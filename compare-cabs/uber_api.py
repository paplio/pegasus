from uber_rides.session import Session 
from uber_rides.client import UberRidesClient
import getLoco

session = Session(server_token="ZzQ0mbOaAK2Vxv_5iEzH2nfK67Zwdb400hwuCeBU")
client = UberRidesClient(session)

response = client.get_products(12.9279630, 77.6290860)
products = response.json.get('products')

response = client.get_price_estimates(
      start_latitude=getLoco.getLat(),
      start_longitude=getLoco.getLon(),
      end_latitude=12.941608,
      end_longitude=77.566883,
      seat_count=1
    ) 
estimates = response.json.get('prices')

###ESTIMATES OF ALL CABS ARE FUNCTIONS TO REDUCE API CALLS###

def uberGoEstimate():
	return estimates[1]['estimate']

def uberXEstimate():
	return estimates[2]['estimate']

def uberXLEstimate():
	return estimates[3]['estimate']


if __name__ == "__main__":
	x = uberGoEstimate()
	print x
