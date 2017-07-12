import requests
import json

#Endpoint:
endpoint = "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCHBR8PagCIe0EAKVdx1SzOfKunYehjSzU"

def getUserSpot():
	r = requests.post(url = endpoint)
	locationDump = r.json()
	lat = locationDump['location']['lat']
	lng = locationDump['location']['lng']
	return lat, lng

if __name__ == "__main__":
	print getUserSpot()

