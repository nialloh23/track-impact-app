from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from database_setup import Regions, Base, ImpactEntry, User
from sqlalchemy import desc

from flask import session as login_session
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests


app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Restaurant Menu Application"


engine = create_engine('sqlite:///impactdatabase.db',connect_args={'check_same_thread':False},poolclass=StaticPool)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

##################################################
########## USER CONTROLLER #######################
##################################################

@app.route('/login')
def userLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check to see if the user is already logged in
    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'


    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h6>Welcome, '
    output += login_session['username']
    output += '!</h6>'
    #output += '<img src="'
    #output += login_session['picture']
    #output += ' " style = "width: 50px; height: 50px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


# DISCONNECT - Revoke a current user's token and reset their login_session


@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['username']
        del login_session['gplus_id']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        return redirect(url_for('showRegion'))
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response



# User Helper Functions


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None



@app.route('/profile/<int:user_id>')
def showProfile(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    impact_enteries = session.query(ImpactEntry).filter_by(user_id=user_id).order_by(desc(ImpactEntry.id)).all()
    return render_template('profile.html', user=user, impact_enteries=impact_enteries, login_session=login_session)

##################################################
########## REGION CONTROLLER ######################
##################################################

@app.route('/home')
def showHome():
    regions = session.query(Regions).all()
    return render_template('index.html')


@app.route('/')
@app.route('/regions')
def showRegion():
#    if 'email' in login_session:
#        picture=login_session['picture']
#    else:
#        picture="https://www.ienglishstatus.com/wp-content/uploads/2018/04/Anonymous-Whatsapp-profile-picture.jpg"
    regions = session.query(Regions).all()
    if 'username' not in login_session:
        return render_template('regionsPublic.html', regions=regions, login_session=login_session)
    else:
        return render_template('regions.html', regions=regions, login_session=login_session)


@app.route('/regionsapi')
def getRegion():
    regions = session.query(Regions).all()
    return jsonify(Regions=[i.serialize for i in regions])



@app.route('/region/new/', methods=['GET', 'POST'])
def newRegion():
    if 'email' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newRegion = Regions(name=request.form['name'], user_id=login_session['user_id'])
        session.add(newRegion)
        session.commit()
        return redirect(url_for('showRegion'))
    else:
        return render_template('newRegion.html',login_session=login_session)


@app.route('/region/<int:region_id>/edit', methods=['GET', 'POST'])
def editRegion(region_id):
    editedRegion = session.query(Regions).filter_by(id=region_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedRegion.name = request.form['name']
            return redirect(url_for('showRegion'))
    else:
        return render_template('editRegion.html', region=editedRegion, login_session=login_session)


@app.route('/region/<int:region_id>/delete', methods=['GET','POST'])
def deleteRegion(region_id):
    regionToDelete = session.query(Regions).filter_by(id=region_id).one()
    if request.method == 'POST':
        session.delete(regionToDelete)
        session.commit()
        return redirect(url_for('showRegion'))
    else:
        return render_template('deleteRegion.html', region=regionToDelete, login_session=login_session)

##################################################
########## IMPACT ENTRY CONTROLLER ################
##################################################

@app.route('/region/<int:region_id>/', methods=['GET', 'POST'])
@app.route('/region/<int:region_id>/impact/', methods=['GET', 'POST'])
def showImpact(region_id):
    region = session.query(Regions).filter_by(id=region_id).one()
    impact_enteries = session.query(ImpactEntry).filter_by(region_id=region_id).order_by(desc(ImpactEntry.id)).all()

    if request.method == 'POST':
        newImpactPost = ImpactEntry(name=request.form['name'], hours=request.form['hours'],
        funding_amount=request.form['funding_amount'],category=request.form['category'], organisation=request.form['organisation'],
        notes=request.form['notes'], picture=request.form['picture'], address=request.form['address'], region_id=region_id, user_id=request.form['user_id'])
        session.add(newImpactPost)
        session.commit()
        return redirect(url_for('showImpact', region_id=region_id))
    else:
        if 'username' not in login_session:
            return render_template('showImpactPublic.html', impact=impact_enteries, region=region, region_id=region_id, login_session=login_session)
        else:
            return render_template('showImpact.html', impact=impact_enteries, region=region, region_id=region_id, login_session=login_session)


@app.route('/region/<int:region_id>/api')
@app.route('/region/<int:region_id>/impact/api')
def getRegionImpact(region_id):
    region = session.query(Regions).filter_by(id=region_id).one()
    impact_enteries = session.query(ImpactEntry).filter_by(region_id=region_id).order_by(desc(ImpactEntry.id)).all()
    return jsonify(ImpactEntry=[i.serialize for i in impact_enteries])



@app.route('/region/<int:region_id>/impact/new/', methods=['GET', 'POST'])
def newImpactEntry(region_id):
    if request.method == 'POST':
        newImpactEntry = ImpactEntry(name=request.form['name'], hours=request.form['hours'],
        funding_amount=request.form['funding_amount'],category=request.form['category'], organisation=request.form['organisation'],
        notes=request.form['notes'], picture=request.form['picture'], address=request.form['address'], region_id=region_id, user_id=request.form['user_id'])
        session.add(newImpactEntry)
        session.commit()
        return redirect(url_for('showImpact', region_id=region_id))
    else:
        return render_template('newImpactEntry.html', region_id=region_id, login_session=login_session)


@app.route('/region/<int:region_id>/impact/<int:impact_id>/edit', methods=['GET', 'POST'])
def editImpactEntry(region_id, impact_id):
    ImpactEntryToEdit = session.query(ImpactEntry).filter_by(id=impact_id).one()
    if request.method == 'POST':
        if request.form['name']:
            ImpactEntryToEdit.name = request.form['name']
        if request.form['hours']:
            ImpactEntryToEdit.description = request.form['hours']
        if request.form['funding_amount']:
            ImpactEntryToEdit.price = request.form['funding_amount']
        if request.form['notes']:
            ImpactEntryToEdit.description = request.form['notes']
        if request.form['address']:
            ImpactEntryToEdit.price = request.form['address']
        if request.form['picture']:
            ImpactEntryToEdit.course = request.form['picture']
        if request.form['category']:
            ImpactEntryToEdit.course = request.form['category']
        session.add(ImpactEntryToEdit)
        session.commit()
        return redirect(url_for('showImpact', region_id=region_id))
    else:
        return render_template('editImpactEntry.html', ImpactEntrytoEdit=ImpactEntryToEdit, region_id=region_id, impact_id=impact_id, login_session=login_session)


@app.route('/region/<int:region_id>/impact/<int:impact_id>/delete', methods=['GET', 'POST'])
def deleteImpactEntry(region_id, impact_id):
        ImpactEntryToDelete = session.query(ImpactEntry).filter_by(id=impact_id).one()
        if request.method == 'POST':
            session.delete(ImpactEntryToDelete)
            session.commit()
            return redirect(url_for('showImpact', region_id=region_id))
        else:
            return render_template('deleteImpactEntry.html', Entry=ImpactEntryToDelete, login_session=login_session)


##################################################
########## Dashboard Controller ##################
##################################################

@app.route('/regions/dashboard')
@app.route('/dashboard')
def showDashboard():
        return 'This page will show the collated impact dashboard from all regions'


@app.route('/region/<int:region_id>/dashboard')
def showRegionDashboard(region_id):
    region = session.query(Regions).filter_by(id=region_id).one()
    return render_template('regionDashboard.html', region=region, login_session=login_session)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
