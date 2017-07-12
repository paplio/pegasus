import requests
import json

send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)


def getLat():
	lat = j['latitude']
	return lat
def getLon():	
	lon = j['longitude']
	return lon

	
