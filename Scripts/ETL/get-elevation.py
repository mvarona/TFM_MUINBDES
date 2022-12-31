#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with the elevation data of each municipality

import sys
import os
import pandas as pd
import re
from dotenv import load_dotenv
import json
import requests
import urllib.parse

def get_elevation(df):
	lat = df['lat']
	lon = df['lon']
	url = "https://api.open-elevation.com/api/v1/lookup?locations=" + str(lat) + "," + str(lon)
	elevation = "-"

	try:
		resp = requests.get(url=url)
		data = resp.json()
		elevation = data['results'][0]['elevation']
	except:
		print("Error con municipio: " + df['municipio_nombre_humano'])

	return elevation

def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 get-elevation.py filename.csv')
		sys.exit(2)
	filename = sys.argv[1]
	new_filename = os.path.splitext(filename)[0] + "_elevation" + ".csv"
	df = pd.read_csv(filename)
	df['elevation'] = df.apply(get_elevation, axis=1)
	df.to_csv(new_filename, index=False)


if __name__ == "__main__":
	main(sys.argv)