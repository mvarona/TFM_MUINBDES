#!/usr/bin/python

import sys
import os
import pandas as pd
import json
import requests
import urllib.parse
from dotenv import load_dotenv

def kelvin_to_celsius(kelvin):
	return round(kelvin - 273.15, 2)

def ms_to_kmh(ms):
	return round(3.6 * ms, 2)

def get_weather(df_municipalities):
	lat = df_municipalities['lat']
	lon = df_municipalities['lon']

	feb_avg_min_temp = "-"
	feb_avg_max_temp = "-"
	feb_avg_temp = "-"
	feb_avg_humidity = "-"
	feb_avg_wind = "-"
	feb_avg_min_rain = "-"
	feb_avg_max_rain = "-"
	feb_avg_rain = "-"
	feb_avg_clouds = "-"
	feb_avg_sunshine_hours = "-"

	jul_avg_min_temp = "-"
	jul_avg_max_temp = "-"
	jul_avg_temp = "-"
	jul_avg_humidity = "-"
	jul_avg_wind = "-"
	jul_avg_min_rain = "-"
	jul_avg_max_rain = "-"
	jul_avg_rain = "-"
	jul_avg_clouds = "-"
	jul_avg_sunshine_hours = "-"

	try:

		url = "http://history.openweathermap.org/data/2.5/aggregated/month?lat=" + str(lat) + "&lon=" + str(lon) + "&month=2&appid=" + os.environ.get('OPENWEATHER_API_KEY')
		resp = requests.get(url=url)
		data = resp.json()

		feb_avg_min_temp = kelvin_to_celsius(data['result']['temp']['average_min'])
		feb_avg_max_temp = kelvin_to_celsius(data['result']['temp']['average_max'])
		feb_avg_temp = kelvin_to_celsius(data['result']['temp']['mean'])
		feb_avg_humidity = data['result']['humidity']['mean']
		feb_avg_wind = ms_to_kmh(data['result']['wind']['mean'])
		feb_avg_min_rain = data['result']['precipitation']['min']
		feb_avg_max_rain = data['result']['precipitation']['max']
		feb_avg_rain = data['result']['precipitation']['mean']
		feb_avg_clouds = data['result']['clouds']['mean']
		feb_avg_sunshine_hours = data['result']['sunshine_hours']

		url = "http://history.openweathermap.org/data/2.5/aggregated/month?lat=" + str(lat) + "&lon=" + str(lon) + "&month=7&appid=" + os.environ.get('OPENWEATHER_API_KEY')

		resp = requests.get(url=url)
		data = resp.json()

		jul_avg_min_temp = kelvin_to_celsius(data['result']['temp']['average_min'])
		jul_avg_max_temp = kelvin_to_celsius(data['result']['temp']['average_max'])
		jul_avg_temp = kelvin_to_celsius(data['result']['temp']['mean'])
		jul_avg_humidity = data['result']['humidity']['mean']
		jul_avg_wind = ms_to_kmh(data['result']['wind']['mean'])
		jul_avg_min_rain = data['result']['precipitation']['min']
		jul_avg_max_rain = data['result']['precipitation']['max']
		jul_avg_rain = data['result']['precipitation']['mean']
		jul_avg_clouds = data['result']['clouds']['mean']
		jul_avg_sunshine_hours = data['result']['sunshine_hours']

	except:
		print("Error con municipio: " + df_municipalities['municipio'] + "(" + df_municipalities['provincia'] + ")")

	return feb_avg_min_temp, feb_avg_max_temp, feb_avg_temp, feb_avg_humidity, feb_avg_wind, feb_avg_min_rain, feb_avg_max_rain, feb_avg_rain, feb_avg_clouds, feb_avg_sunshine_hours, jul_avg_min_temp, jul_avg_max_temp, jul_avg_temp, jul_avg_humidity, jul_avg_wind, jul_avg_min_rain, jul_avg_max_rain, jul_avg_rain, jul_avg_clouds, jul_avg_sunshine_hours

def get_feb_avg_min_temp(row):
	data = row[0]
	return data

def get_feb_avg_max_temp(row):
	data = row[1]
	return data

def get_feb_avg_temp(row):
	data = row[2]
	return data

def get_feb_avg_humidity(row):
	data = row[3]
	return data

def get_feb_avg_wind(row):
	data = row[4]
	return data

def get_feb_avg_min_rain(row):
	data = row[5]
	return data

def get_feb_avg_max_rain(row):
	data = row[6]
	return data

def get_feb_avg_rain(row):
	data = row[7]
	return data

def get_feb_avg_clouds(row):
	data = row[8]
	return data

def get_feb_avg_sunshine_hours(row):
	data = row[9]
	return data

def get_jul_avg_min_temp(row):
	data = row[10]
	return data

def get_jul_avg_max_temp(row):
	data = row[11]
	return data

def get_jul_avg_temp(row):
	data = row[12]
	return data

def get_jul_avg_humidity(row):
	data = row[13]
	return data

def get_jul_avg_wind(row):
	data = row[14]
	return data

def get_jul_avg_min_rain(row):
	data = row[15]
	return data

def get_jul_avg_max_rain(row):
	data = row[16]
	return data

def get_jul_avg_rain(row):
	data = row[17]
	return data

def get_jul_avg_clouds(row):
	data = row[18]
	return data

def get_jul_avg_sunshine_hours(row):
	data = row[19]
	return data

def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 get-weather.py municipalities_geocoded.csv')
		sys.exit(2)

	municipalities = sys.argv[1]
	new_filename = os.path.splitext(municipalities)[0] + "_weather" + ".csv"
	df_municipalities = pd.read_csv(municipalities)

	df_municipalities['weather'] = df_municipalities.apply(get_weather, axis=1)
	df_municipalities['feb_avg_min_temp'] = df_municipalities['weather'].apply(get_feb_avg_min_temp)
	df_municipalities['feb_avg_max_temp'] = df_municipalities['weather'].apply(get_feb_avg_max_temp)
	df_municipalities['feb_avg_temp'] = df_municipalities['weather'].apply(get_feb_avg_temp)
	df_municipalities['feb_avg_humidity'] = df_municipalities['weather'].apply(get_feb_avg_humidity)
	df_municipalities['feb_avg_wind'] = df_municipalities['weather'].apply(get_feb_avg_wind)
	df_municipalities['feb_avg_min_rain'] = df_municipalities['weather'].apply(get_feb_avg_min_rain)
	df_municipalities['feb_avg_max_rain'] = df_municipalities['weather'].apply(get_feb_avg_max_rain)
	df_municipalities['feb_avg_rain'] = df_municipalities['weather'].apply(get_feb_avg_rain)
	df_municipalities['feb_avg_clouds'] = df_municipalities['weather'].apply(get_feb_avg_clouds)
	df_municipalities['feb_avg_sunshine_hours'] = df_municipalities['weather'].apply(get_feb_avg_sunshine_hours)

	df_municipalities['jul_avg_min_temp'] = df_municipalities['weather'].apply(get_jul_avg_min_temp)
	df_municipalities['jul_avg_max_temp'] = df_municipalities['weather'].apply(get_jul_avg_max_temp)
	df_municipalities['jul_avg_temp'] = df_municipalities['weather'].apply(get_jul_avg_temp)
	df_municipalities['jul_avg_humidity'] = df_municipalities['weather'].apply(get_jul_avg_humidity)
	df_municipalities['jul_avg_wind'] = df_municipalities['weather'].apply(get_jul_avg_wind)
	df_municipalities['jul_avg_min_rain'] = df_municipalities['weather'].apply(get_jul_avg_min_rain)
	df_municipalities['jul_avg_max_rain'] = df_municipalities['weather'].apply(get_jul_avg_max_rain)
	df_municipalities['jul_avg_rain'] = df_municipalities['weather'].apply(get_jul_avg_rain)
	df_municipalities['jul_avg_clouds'] = df_municipalities['weather'].apply(get_jul_avg_clouds)
	df_municipalities['jul_avg_sunshine_hours'] = df_municipalities['weather'].apply(get_jul_avg_sunshine_hours)

	df_municipalities = df_municipalities.drop('weather', axis=1)
	df_municipalities.to_csv(new_filename, index=False)

if __name__ == "__main__":
	load_dotenv()
	main(sys.argv)