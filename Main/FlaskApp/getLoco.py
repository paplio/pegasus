import googlemaps
import sys

gm = googlemaps.Client(key = "AIzaSyAdBrRjT1naXA3PbjKcMyZU1WP0SIoFvCU")

def getLocation(address_string):
	coords = gm.geocode(address_string)
	lat = coords[0]['geometry']['location']['lat']
	lon = coords[0]['geometry']['location']['lng']
	return lat, lon

if __name__ == "__main__":
	query = sys.argv[1] 
	x = getLocation(query)
	print x