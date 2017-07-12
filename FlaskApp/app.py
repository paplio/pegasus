###INITIALISING AND IMPORTING SHIT###
from flask import Flask 
from flask import request
from flask import render_template
import sys
import getLoco
import getLocationUser
import ola_api

app = Flask(__name__)

###DEFINING ALL ROUTES###

@app.route("/")
def main(name=None):
	return render_template('index.html')

@app.route("/result", methods = ['POST', 'GET'])
def getResult():
	if request.method == 'POST':
		text = request.form['text']
		droplat, droplon = getLoco.getLocation(text)
		picklat, picklon = getLocationUser.getUserSpot()
		print picklat, picklon, droplat, droplon
		##CALLING OLA CABS API TO GET ESTIMATES OF MINI AND SEDAN##
		miniData = ola_api.getDataDump(picklat, picklon, droplat, droplon, 'mini')
		primeData = ola_api.getDataDump(picklat, picklon, droplat, droplon, 'prime')
		print miniData
		print primeData
		return render_template("compare.html", olaMini = miniData, olaPrime = primeData)

if __name__ == "__main__":
	app.run(debug = True)

