from uber_rides.session import Session 
from uber_rides.client import UberRidesClient
import getLoco
import getLocationUser

session = Session(server_token="ZzQ0mbOaAK2Vxv_5iEzH2nfK67Zwdb400hwuCeBU")
client = UberRidesClient(session)

def getPrice(droplat, droplng):
  #response = client.get_products(getLocationUser.getUserSpot())
  #products = response.json.get('products')
  picklat, picklng = getLocationUser.getUserSpot()
  response = client.get_price_estimates(
    start_latitude=picklat,
    start_longitude=picklng,
    end_latitude=droplat,
    end_longitude=droplng,
    seat_count=2
    ) 
  estimates = response.json.get('prices')
  return estimates[1]['estimate'], estimates[2]['estimate'], estimates[3]['estimate']
###ESTIMATES OF ALL CABS ARE FUNCTIONS TO REDUCE API CALLS###

def uberGoEstimate():
	return estimates[1]['estimate']

def uberXEstimate():
	return estimates[2]['estimate']

def uberXLEstimate():
	return estimates[3]['estimate']


if __name__ == "__main__":
	x = getPrice(12.9416, 77.5669)
	print x
