#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with the top places encoded with one-hot encoding

import sys
import os
import pandas as pd
import re
import json
import requests
import urllib.parse
import numpy as np
import time

def get_coast_line(df_municipalities):

	first_place = ""
	second_place = ""
	third_place = ""

	if len(df_municipalities['top_3_sitios'].split(";")) > 0:
		first_place = df_municipalities['top_3_sitios'].split(";")[0]

	if len(df_municipalities['top_3_sitios'].split(";")) > 1:
		second_place = df_municipalities['top_3_sitios'].split(";")[1]

	if len(df_municipalities['top_3_sitios'].split(";")) > 2:
		third_place = df_municipalities['top_3_sitios'].split(";")[2]

	commercial = 0
	tourism = 0
	accommodation = 0
	leisure = 0
	natural = 0
	service = 0
	activity = 0
	entertainment = 0
	catering = 0
	sport = 0
	building = 0
	access_limited = 0
	man_made = 0
	access = 0
	no_access = 0
	heritage = 0
	highway = 0
	fee = 0
	amenity = 0

	if first_place == 'commercial':
		commercial = 1
	elif first_place == 'tourism':
		tourism = 1
	elif first_place == 'accommodation':
		accommodation = 1
	elif first_place == 'leisure':
		leisure = 1
	elif first_place == 'natural':
		natural = 1
	elif first_place == 'service':
		service = 1
	elif first_place == 'activity':
		activity = 1
	elif first_place == 'entertainment':
		entertainment = 1
	elif first_place == 'catering':
		catering = 1
	elif first_place == 'sport':
		sport = 1
	elif first_place == 'building':
		building = 1
	elif first_place == 'access_limited':
		access_limited = 1
	elif first_place == 'man_made':
		man_made = 1
	elif first_place == 'access':
		access = 1
	elif first_place == 'no_access':
		no_access = 1
	elif first_place == 'heritage':
		heritage = 1
	elif first_place == 'highway':
		highway = 1
	elif first_place == 'fee':
		fee = 1
	elif first_place == 'amenity':
		amenity = 1

	if second_place == 'commercial':
		commercial = 2
	elif second_place == 'tourism':
		tourism = 2
	elif second_place == 'accommodation':
		accommodation = 2
	elif second_place == 'leisure':
		leisure = 2
	elif second_place == 'natural':
		natural = 2
	elif second_place == 'service':
		service = 2
	elif second_place == 'activity':
		activity = 2
	elif second_place == 'entertainment':
		entertainment = 2
	elif second_place == 'catering':
		catering = 2
	elif second_place == 'sport':
		sport = 2
	elif second_place == 'building':
		building = 2
	elif second_place == 'access_limited':
		access_limited = 2
	elif second_place == 'man_made':
		man_made = 2
	elif second_place == 'access':
		access = 2
	elif second_place == 'no_access':
		no_access = 2
	elif second_place == 'heritage':
		heritage = 2
	elif second_place == 'highway':
		highway = 2
	elif second_place == 'fee':
		fee = 2
	elif second_place == 'amenity':
		amenity = 2

	if third_place == 'commercial':
		commercial = 3
	elif third_place == 'tourism':
		tourism = 3
	elif third_place == 'accommodation':
		accommodation = 3
	elif third_place == 'leisure':
		leisure = 3
	elif third_place == 'natural':
		natural = 3
	elif third_place == 'service':
		service = 3
	elif third_place == 'activity':
		activity = 3
	elif third_place == 'entertainment':
		entertainment = 3
	elif third_place == 'catering':
		catering = 3
	elif third_place == 'sport':
		sport = 3
	elif third_place == 'building':
		building = 3
	elif third_place == 'access_limited':
		access_limited = 3
	elif third_place == 'man_made':
		man_made = 3
	elif third_place == 'access':
		access = 3
	elif third_place == 'no_access':
		no_access = 3
	elif third_place == 'heritage':
		heritage = 3
	elif third_place == 'highway':
		highway = 3
	elif third_place == 'fee':
		fee = 3
	elif third_place == 'amenity':
		amenity = 3

	return commercial,tourism,accommodation,leisure,natural,service,activity,entertainment,catering,sport,building,access_limited,man_made,access,no_access,heritage,highway,fee,amenity

def get_commercial(row):
	return row[0]

def get_tourism(row):
	return row[1]

def get_accomodation(row):
	return row[2]

def get_leisure(row):
	return row[3]

def get_natural(row):
	return row[4]

def get_service(row):
	return row[5]

def get_activity(row):
	return row[6]

def get_entertainment(row):
	return row[7]

def get_catering(row):
	return row[8]

def get_sport(row):
	return row[9]

def get_building(row):
	return row[10]

def get_access_limited(row):
	return row[11]

def get_man_made(row):
	return row[12]

def get_access(row):
	return row[13]

def get_no_access(row):
	return row[14]

def get_heritage(row):
	return row[15]

def get_highway(row):
	return row[16]

def get_fee(row):
	return row[17]

def get_amenity(row):
	return row[18]


def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 encode-places.py municipalities.csv')
		sys.exit(2)
	municipalities_fn = sys.argv[1]
	new_municipalities_fn = os.path.splitext(municipalities_fn)[0] + "_encoded" + ".csv"
	municipalities = pd.read_csv(municipalities_fn)
	
	municipalities['places'] = municipalities.apply(get_coast_line, axis=1)
	municipalities['sitios_comercio'] = municipalities['places'].apply(get_commercial)
	municipalities['sitios_turismo'] = municipalities['places'].apply(get_tourism)
	municipalities['sitios_alojamiento'] = municipalities['places'].apply(get_accomodation)
	municipalities['sitios_ocio'] = municipalities['places'].apply(get_leisure)
	municipalities['sitios_natural'] = municipalities['places'].apply(get_natural)
	municipalities['sitios_servicio'] = municipalities['places'].apply(get_service)
	municipalities['sitios_actividad'] = municipalities['places'].apply(get_activity)
	municipalities['sitios_entretenimiento'] = municipalities['places'].apply(get_entertainment)
	municipalities['sitios_catering'] = municipalities['places'].apply(get_catering)
	municipalities['sitios_sport'] = municipalities['places'].apply(get_sport)
	municipalities['sitios_edificio'] = municipalities['places'].apply(get_building)
	municipalities['sitios_acceso_limitado'] = municipalities['places'].apply(get_access_limited)
	municipalities['sitios_artificial'] = municipalities['places'].apply(get_man_made)
	municipalities['sitios_acceso'] = municipalities['places'].apply(get_access)
	municipalities['sitios_sin_acceso'] = municipalities['places'].apply(get_no_access)
	municipalities['sitios_patrimonio'] = municipalities['places'].apply(get_heritage)
	municipalities['sitios_carretera'] = municipalities['places'].apply(get_highway)
	municipalities['sitios_cuota'] = municipalities['places'].apply(get_fee)
	municipalities['sitios_comodidad'] = municipalities['places'].apply(get_amenity)
	
	municipalities = municipalities.drop(['places','top_3_sitios','sitio_mas_frecuente'], axis=1)
	municipalities.to_csv(new_municipalities_fn, index=False)

if __name__ == "__main__":
	main(sys.argv)