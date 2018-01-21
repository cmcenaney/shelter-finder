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

	df = pd.read_csv('shelters.csv')
	df['infobox'] = df.apply(lambda row: '<a href="{}" target="_blank">{}</a>'.format(row['url'], row['name']), axis=1)
	
	markers = df.to_dict(orient='records')

	initmap = Map(
		identifier="map",
		lat= 35.402084,
		lng= -79.784205,
		markers = markers,
		style = "height:400px;width:100%;margin:10;",
		zoom = 6
	)

	if not address:
		return render_template('index.html', address=address, found=None, location=None, df=df, map=initmap)

	geolocator = Nominatim()
	location = geolocator.geocode(address)

	if not location:
		return render_template('index.html', address=address, found=False, location=None, df=df, map=initmap)

	df = find_distance((location.latitude, location.longitude))
	sheltermap = Map(
		identifier="map",
		lat= location.latitude,
		lng= location.longitude,
		markers = markers,
		style = "height:400px;width:100%;margin:10;",
		zoom = 10
	)

	df = df[['name', 'address', 'dist']]
	df.columns = ['Shelter', 'Address', 'Distance']
	return render_template('index.html', address=address, found=True, location=location, df=df, map=sheltermap)


def find_distance(loc):
	df = pd.read_csv('shelters.csv')
	df['coord'] = df.apply(lambda row: (row.lat, row.lng), axis=1)
	df['dist'] = df['coord'].apply(lambda x: vincenty(x, loc).miles)
	df['infobox'] = df['name']
	df = df.sort_values('dist')
	return df






