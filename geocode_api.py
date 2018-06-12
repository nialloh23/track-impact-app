import httplib2
import json

def getGeocodeLocation(inputString):
    google_api_key="AIzaSyAz0m-9jsGJ5u2it9wYrfxL55VFxs3t_MA"
    locationString= inputString.replace(" ", "+")
    url=('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(
    locationString, google_api_key))
    h=httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    latitude=result['results'][0]['geometry']['location']['lat']
    longitude=result['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)
latitude,Longitude = getGeocodeLocation()

print (latitude)
print (longitude)
