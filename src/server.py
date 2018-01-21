from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import pandas as pd



app = Flask(__name__)

app.config['GOOGLEMAPS_KEY'] = 'AIzaSyD_jsi5AzwyTvBQNX4teISdvQ-T5r9YIJA'
GoogleMaps(app)

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

	
	sheltermap = Map(
		identifier="map",
		lat= location.latitude,
		lng= location.longitude,
		markers=[
			{
			'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
			'lat': location.latitude,
			'lng': location.longitude,
			'infobox': "<b>Hello</b>"
			},
			{
			'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
			'lat': 37.4300,
			'lng': -122.1400,
			'infobox': "<b>Hello World from other place</b>"
			}
		]
	)


			


		



	return render_template('index.html', address=address, found=found, location=location, df=df, map=sheltermap)


def find_distance(loc):
	df = pd.read_csv('shelters.csv')
	df['coord'] = df.apply(lambda row: (row.lat, row.long), axis=1)
	df['dist'] = df['coord'].apply(lambda x: vincenty(x, loc).miles)
	df = df.sort_values('dist')
	return df

def mapview():
	mymap = Map(
		identifier="view-side",
		lat=37.4419,
		lng=-122.1419,
		markers=[(37.4419, -122.1419)]
	)
	sndmap = Map(
		identifier="sndmap",
		lat=37.4419,
		lng=-122.1419,
		markers=[
			{
			'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
			'lat': 37.4419,
			'lng': -122.1419,
			'infobox': "<b>Hello World</b>"
			},
			{
			'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
			'lat': 37.4300,
			'lng': -122.1400,
			'infobox': "<b>Hello World from other place</b>"
			}
		]
	)
	return render_template('index.html', mymap=mymap, sndmap=sndmap)




