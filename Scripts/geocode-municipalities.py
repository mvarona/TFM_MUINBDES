#!/usr/bin/python

import sys
import os
import pandas as pd
import re
from dotenv import load_dotenv
import json
import requests
import urllib.parse

def geocode_municipalities(df):
	municipality = urllib.parse.quote(df['municipio_nombre_humano'])
	if ("/" in municipality):
		municipality = municipality.split("/")[0]

	province = urllib.parse.quote(df['provincia'])
	url = "http://api.positionstack.com/v1/forward?access_key=" + os.environ.get('POSITIONSTACK_ACCESS_KEY') + "&query=" + municipality + "," + province

	resp = requests.get(url=url)
	data = resp.json()

	lat = 0
	lon = 0
	
	try:
		lat = data['data'][0]['latitude']
		lon = data['data'][0]['longitude']
	except:
		print("Error con municipio: " + df['municipio_nombre_humano'] + "(" + municipality + "), provincia: " + df['provincia'] + "(" + province + ")")

	return lat, lon

def get_lat(row):
	lat = row[0]
	return lat

def get_lon(row):
	lon = row[1]
	return lon

def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 geocode-municipalities.py filename.csv')
		sys.exit(2)
	filename = sys.argv[1]
	new_filename = os.path.splitext(filename)[0] + "_geocoded" + ".csv"
	df = pd.read_csv(filename)
	df['geocode'] = df.apply(geocode_municipalities, axis=1)
	df['lat'] = df['geocode'].apply(get_lat)
	df['lon'] = df['geocode'].apply(get_lon)
	df = df.drop('geocode', axis=1)
	df.to_csv(new_filename, index=False)


if __name__ == "__main__":
	load_dotenv()
	main(sys.argv)