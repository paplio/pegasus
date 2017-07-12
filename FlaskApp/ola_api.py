import requests
import json
import sys

def getDataDump(picklat, picklng, droplat, droplng, type):
	headers = {'X-APP-TOKEN' : "317aaa2757bd4f56a3295a59a8a3bd5d"}

	if type == 'mini':
		payload = {'pickup_lat':picklat, 'pickup_lng':picklng, 'drop_lat':droplat, 'drop_lng':droplng,'category':'micro'}
	elif type == 'prime':
				payload = {'pickup_lat':picklat, 'pickup_lng':picklng, 'drop_lat':droplat, 'drop_lng':droplng,'category':'prime'}

	r = requests.get("http://sandbox-t.olacabs.com/v1/products/", params = payload, headers = headers)
	data_dump = r.json()
	minamt = data_dump['ride_estimate'][0]['amount_min']
	maxamt = data_dump['ride_estimate'][0]['amount_max']
	print data_dump
	print str(minamt) + " to " + str(maxamt)
	return str(minamt) + " to Rs." + str(maxamt)






if __name__ == "__main__":
	getDataDump(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])