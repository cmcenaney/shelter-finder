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


			# df = df[['name', 'address', 'dist']]

			# df['url'] = df['url'].apply(lambda x: '<a href="{}">{}</a>'.format(x, x))ś
			# df['url'] = df['url'].apply(lambda x: '<a href="{}>ht</a>'.format(x))ś


			print(df.to_dict(orient='records'))

			markers = df.to_dict(orient='records')

			sheltermap = Map(
				identifier="map",
				lat= location.latitude,
				lng= location.longitude,
				markers = markers,
				style = "height:400px;width:100%;margin:10;",
				zoom = 8
				# markers=[
				# 	{
				# 	'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
				# 	'lat': location.latitude,
				# 	'lng': location.longitude,
				# 	'infobox': "<b>Hello</b>"
				# 	},
				# 	{
				# 	'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
				# 	'lat': 37.4300,
				# 	'lng': -122.1400,
				# 	'infobox': "<b>Hello World from other place</b>"
				# 	}
				# ]
			)


			# [{'name': 'Shelter for Battered Women', 
			# 'address': '600 E 5th St, Charlotte, NC 28202, USA', 
			# 'lat': 35.22291, 'long': -80.83591700000001, 'url': 'http://www.domesticviolence-wilm.org/', 'coord': (35.22291, -80.83591700000001), 'dist': 99.6289033528862}, {'name': "Onslow Women's Center Inc", 'address': '226 New Bridge St, Jacksonville, NC 28540, USA', 'lat': 34.749013, 'long': -77.41960879999999, 'url': 'http://www.domesticviolence-wilm.org/', 'coord': (34.749013, -77.41960879999999), 'dist': 119.84833908161018}, {'name': 'Domestic Violence Shelter - The Open Gate', 'address': '2901 Market St, Wilmington, NC 28401, USA', 'lat': 34.235848, 'long': -77.943268, 'url': 'http://www.domesticviolence-wilm.org/', 'coord': (34.235848, -77.943268), 'dist': 123.97659444126984}, {'name': "Coastal Women's Shelter", 'address': '1333 S Glenburnie Rd, New Bern, NC 28562, USA', 'lat': 35.105613, 'long': -77.099946, 'url': 'http://www.domesticviolence-wilm.org/', 'coord': (35.105613, -77.099946), 'dist': 124.65026890597738}]
			
		
		







		else:
			found = False


	
	


			


		



	return render_template('index.html', address=address, found=found, location=location, df=df, map=sheltermap)


def find_distance(loc):
	df = pd.read_csv('shelters.csv')
	df['coord'] = df.apply(lambda row: (row.lat, row.lng), axis=1)
	df['dist'] = df['coord'].apply(lambda x: vincenty(x, loc).miles)
	df['infobox'] = df['name']
	df = df.sort_values('dist')
	return df






