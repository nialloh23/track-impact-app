from flask import Flask

app = Flask(__name__)


########## USER CONTROLLER #######################
##################################################

@app.route('/login')
def userLogin():
    return 'This page will show the login modal for users'

@app.route('/profile')
def userProfile():
    return 'This page will show users profile page'

########## REGION CONTROLLER ######################
##################################################

@app.route('/')
@app.route('/regions')
def showRegion():
    return 'This page will show the full list of regions'

@app.route('/region/new')
def newRegion():
    return 'This page will be for adding a new region'

@app.route('/region/<int:region_id>/edit')
def editRegion():
    return 'This page will be for editing an existing region'

@app.route('/region/<int:region_id>/delete')
def deleteRegion():
    return 'This page will be for deleting an existing region'

########## IMPACT ENTRY CONTROLLER ######################
##################################################

@app.route('/region/<int:region_id>/')
@app.route('/region/<int:region_id>/impact/')
def showImpact():
        return 'This page will be showing the impact activity of a single region'


@app.route('/region/<int:region_id>/impact/new/', methods=['GET', 'POST'])
def newImpactEntry():
        return 'This page will be for creating a new impact entry for a given region'


@app.route('/region/<int:region_id>/impact/<int:impact_id>/edit', methods=['GET', 'POST'])
def editImpactEntry():
        return 'This page will be for editing an impact entry of a given region'


@app.route('/region/<int:region_id>/impact/<int:impact_id>/delete', methods=['GET', 'POST'])
def deleteImpactEntry():
        return 'This page will be for deleting an impact entry of a given region'


########## DASHBOARD CONTROLLER ######################
##################################################

@app.route('/regions/dashboard')
def showDashboard():
        return 'This page will show the collated impact dashboard from all regions'

@app.route('/region/<int:region_id>/dashboard')
def showRegionDashboard():
        return 'This page will show the impact dashboard for a given region'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
