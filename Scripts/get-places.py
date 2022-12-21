#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022

# Returns a CSV with the main places on a 5km radius around the specified coordinates

import sys
import os
import pandas as pd
import re
from dotenv import load_dotenv
import json
import requests
import urllib.parse
import operator

def get_frecuent_places(df):
	municipality = df['municipio_nombre_humano']
	province = df['provincia']
	lat = df['lat']
	lon = df['lon']
	url = "https://api.geoapify.com/v2/places?categories=commercial,tourism,accommodation,leisure,natural,service,activity,entertainment,catering,sport&filter=circle:" + str(lon) + "," + str(lat) + ",5000&bias=proximity:" + str(lon) + "," + str(lat) + "&limit=20&apiKey=" + os.environ.get('GEOAPIFY_API_KEY')
	
	top_3_places = "[-]"
	place_most_frecuent = "-"

	try:
		resp = requests.get(url=url)
		data = resp.json()
		places_categories = {}
		features = data['features']
		for feature in features:
			if feature['properties']['categories'][0] not in places_categories:
				places_categories[feature['properties']['categories'][0]] = 1
			places_categories[feature['properties']['categories'][0]] += 1
		
		places_categories = dict(sorted(places_categories.items(), key=operator.itemgetter(1), reverse=True))
		top_3_places = list(places_categories.keys())[:3]
		
		if len(top_3_places) > 0:
			place_most_frecuent = top_3_places[0]
			top_3_places = ";".join(top_3_places)
		else:
			top_3_places = "[-]"
			place_most_frecuent = "-"

	except:
		print("Error con municipio: " + municipality + "(" + province + ")" )

	return top_3_places, place_most_frecuent

def get_top_3_places(row):
	return row[0]

def get_most_frecuent_place(row):
	return row[1]

def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 get-places.py filename-geocoded.csv')
		sys.exit(2)
	filename = sys.argv[1]
	new_filename = os.path.splitext(filename)[0] + "_places" + ".csv"
	df = pd.read_csv(filename)

	df['top_3_sitios_mas_frecuentes'] = df.apply(get_frecuent_places, axis=1)
	df['top_3_sitios'] = df['top_3_sitios_mas_frecuentes'].apply(get_top_3_places)
	df['sitio_mas_frecuente'] = df['top_3_sitios_mas_frecuentes'].apply(get_most_frecuent_place)

	df = df.drop('top_3_sitios_mas_frecuentes', axis=1)
	df.to_csv(new_filename, index=False)

if __name__ == "__main__":
	load_dotenv()
	main(sys.argv)