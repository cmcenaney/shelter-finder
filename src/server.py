from flask import Flask, render_template, request
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import pandas as pd



app = Flask(__name__)



# FLASK_APP=server.py FLASK_DEBUG=1 flask run



@app.route('/')
def index():



	address = request.args.get('address', None)

	found = None
	location = None
	df = None

	if address:
		print (address)
		geolocator = Nominatim()
		location = geolocator.geocode(address)

		if location:
			found = True


			df = find_distance((location.latitude, location.longitude))
			df = df[['name', 'address', 'dist']]

			# df['url'] = df['url'].apply(lambda x: '<a href="{}">{}</a>'.format(x, x))

			# df['url'] = df['url'].apply(lambda x: '<a href="{}>ht</a>'.format(x))



			








		else:
			found = False


			


		



	return render_template('index.html', address=address, found=found, location=location, df=df)


def find_distance(loc):
	df = pd.read_csv('shelters.csv')
	df['coord'] = df.apply(lambda row: (row.lat, row.long), axis=1)
	df['dist'] = df['coord'].apply(lambda x: vincenty(x, loc).miles)
	df = df.sort_values('dist')
	return df




