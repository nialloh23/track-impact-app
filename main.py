from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from database_setup import Regions, Base, ImpactEntry, User
from sqlalchemy import desc

app = Flask(__name__)


engine = create_engine('sqlite:///impactdatabase.db',connect_args={'check_same_thread':False},poolclass=StaticPool)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

##################################################
########## USER CONTROLLER #######################
##################################################

@app.route('/login')
def userLogin():
    return 'This page will show the login modal for users'

@app.route('/profile/<int:user_id>')
def showProfile(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    impact_enteries = session.query(ImpactEntry).filter_by(user_id=user_id).order_by(desc(ImpactEntry.id)).all()
    return render_template('profile.html', user=user, impact_enteries=impact_enteries)

##################################################
########## REGION CONTROLLER ######################
##################################################

@app.route('/home')
def showHome():
    regions = session.query(Regions).all()
    return render_template('index.html', regions=regions)


@app.route('/')
@app.route('/regions')
def showRegion():
    regions = session.query(Regions).all()
    return render_template('regions.html', regions=regions)


@app.route('/region/new/', methods=['GET', 'POST'])
def newRegion():
    if request.method == 'POST':
        newRegion = Regions(name=request.form['name'])
        session.add(newRegion)
        session.commit()
        return redirect(url_for('showRegion'))
    else:
        return render_template('newRegion.html')



@app.route('/region/<int:region_id>/edit', methods=['GET', 'POST'])
def editRegion(region_id):
    editedRegion = session.query(Regions).filter_by(id=region_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedRegion.name = request.form['name']
            return redirect(url_for('showRegion'))
    else:
        return render_template('editRegion.html', region=editedRegion)


@app.route('/region/<int:region_id>/delete', methods=['GET','POST'])
def deleteRegion(region_id):
    regionToDelete = session.query(Regions).filter_by(id=region_id).one()
    if request.method == 'POST':
        session.delete(regionToDelete)
        session.commit()
        return redirect(url_for('showRegion'))
    else:
        return render_template('deleteRegion.html', region=regionToDelete)

##################################################
########## IMPACT ENTRY CONTROLLER ################
##################################################

@app.route('/region/<int:region_id>/')
@app.route('/region/<int:region_id>/impact/')
def showImpact(region_id):
    region = session.query(Regions).filter_by(id=region_id).one()
    impact_enteries = session.query(ImpactEntry).filter_by(region_id=region_id).order_by(desc(ImpactEntry.id)).all()
    return render_template('impact.html', impact=impact_enteries, region=region)



@app.route('/region/<int:region_id>/impact/new/', methods=['GET', 'POST'])
def newImpactEntry(region_id):
    if request.method == 'POST':
        newImpactEntry = ImpactEntry(name=request.form['name'], hours=request.form['hours'],
        funding_amount=request.form['funding_amount'],category=request.form['category'], organisation=request.form['category'],
        notes=request.form['notes'], picture=request.form['picture'], address=request.form['address'], region_id=region_id, user_id=request.form['user_id'])
        session.add(newImpactEntry)
        session.commit()
        return redirect(url_for('showImpact', region_id=region_id))
    else:
        return render_template('newImpactEntry.html', region_id=region_id)


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
        return render_template('editImpactEntry.html', ImpactEntrytoEdit=ImpactEntryToEdit, region_id=region_id, impact_id=impact_id)


@app.route('/region/<int:region_id>/impact/<int:impact_id>/delete', methods=['GET', 'POST'])
def deleteImpactEntry(region_id, impact_id):
        ImpactEntryToDelete = session.query(ImpactEntry).filter_by(id=impact_id).one()
        if request.method == 'POST':
            session.delete(ImpactEntryToDelete)
            session.commit()
            return redirect(url_for('showImpact', region_id=region_id))
        else:
            return render_template('deleteImpactEntry.html', Entry=ImpactEntryToDelete)


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
    return render_template('regionDashboard.html', region=region)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
