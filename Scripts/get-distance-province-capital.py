#!/usr/bin/python

import sys
import os
import pandas as pd
import json
import requests
import urllib.parse

def get_kms_capital_province(df_municipalities, df_capital_provinces, df_municipalities_geocoded):
	kms = -1

	municipality = df_municipalities['municipio_nombre_humano']
	province = df_municipalities['provincia']
	capital = df_capital_provinces[df_capital_provinces['provincia'] == province]['capital'].astype(str).values[0]
	
	municipality_lat = df_municipalities['lat']
	municipality_lon = df_municipalities['lon']

	capital_lat = df_municipalities_geocoded[df_municipalities_geocoded['municipio_nombre_humano'] == capital]['lat'].astype(float).values[0]
	capital_lon = df_municipalities_geocoded[df_municipalities_geocoded['municipio_nombre_humano'] == capital]['lon'].astype(float).values[0]

	url = "http://169.254.20.42:8080/otp/routers/default/plan?fromPlace=" + str(municipality_lat) + "," + str(municipality_lon) + "&toPlace=" + str(capital_lat) + "," + str(capital_lon) + "&time=12%3A16pm&date=07-20-2022&mode=CAR&arriveBy=false&showIntermediateStops=true&locale=es"
	
	try:
		resp = requests.get(url=url)
		data = resp.json()
		if (municipality_lat == capital_lat and municipality_lon == capital_lon):
			kms = 0
		else:
			kms = data['plan']['itineraries'][0]['walkDistance'] / 1000
	except:

		try:
			url = "http://169.254.20.42:8080/otp/routers/default/plan?fromPlace=" + str(municipality_lat) + "," + str(municipality_lon) + "&toPlace=" + str(capital_lat) + "," + str(capital_lon) + "&time=12%3A16pm&date=07-20-2022&mode=FLEX_DIRECT&arriveBy=false&showIntermediateStops=true&locale=es"

			resp = requests.get(url=url)
			data = resp.json()
			if (municipality_lat == capital_lat and municipality_lon == capital_lon):
				kms = 0
			else:
				kms = data['plan']['itineraries'][0]['walkDistance'] / 1000
		except:
			print("Error con municipio: " + municipality + "(" + str(municipality_lat) + "," + str(municipality_lon) + ")")

	return kms

def main(argv):
	if (len(sys.argv) < 3):
		print('Uso: python3 get-distance-province-capital.py municipalities.csv capital_provinces.csv')
		sys.exit(2)

	municipalities = sys.argv[1]
	capital_provinces = sys.argv[2]
	new_filename = os.path.splitext(municipalities)[0] + "_distances" + ".csv"
	df_municipalities = pd.read_csv(municipalities)
	df_capital_provinces = pd.read_csv(capital_provinces)

	df_municipalities['kms_capital_provincia'] = df_municipalities.apply(get_kms_capital_province, axis=1, args=(df_capital_provinces, df_municipalities, ))
	df_municipalities.to_csv(new_filename, index=False)

if __name__ == "__main__":
	main(sys.argv)