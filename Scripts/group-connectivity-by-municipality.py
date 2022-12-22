#!/usr/bin/python


# Mario Varona Bueno
# TFM MUINBDES
# 2022

# Returns a CSV with the maximum available bandwith per municipality (instead of per singular entity, as in the government data)

import sys
import os
import pandas as pd
import re
import json
import requests
import urllib.parse
import numpy as np
import time

def convert_to_title(row):
	return row.title()

def get_nsi_code(df_municipalities, municipalities):
	try:
		municipality = df_municipalities.name
		esp_code = municipalities[municipalities['entidad_singular_poblacion'] == municipality]['codigo_esp'].astype(str).values[0]
		nsi_code = esp_code[0:5]
		return nsi_code
	except:
		pass

def get_region(df_municipalities, municipalities):
	try:
		municipality = df_municipalities.name
		region = municipalities[municipalities['entidad_singular_poblacion'] == municipality]['comunidad_autonoma'].astype(str).values[0]
		return region
	except:
		pass

def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 group-connectivity.py municipalities-SPEs-connectivity.csv')
		sys.exit(2)
	municipalities_fn = sys.argv[1]
	new_municipalities_fn = os.path.splitext(municipalities_fn)[0] + "_connectivity" + ".csv"
	municipalities = pd.read_csv(municipalities_fn)
	municipalities = municipalities.drop('habitantes', axis=1)
	municipalities_grouped = municipalities.groupby('municipio').mean()
	
	municipalities['entidad_singular_poblacion'] = municipalities['entidad_singular_poblacion'].apply(convert_to_title)
	municipalities_grouped['codigo_ine'] = municipalities_grouped.apply(get_nsi_code, axis=1, args=(municipalities, ))
	municipalities_grouped['comunidad_autonoma'] = municipalities_grouped.apply(get_region, axis=1, args=(municipalities, ))
	
	municipalities_grouped['cobertura_30'] = municipalities_grouped['cobertura_30'].round(2)
	municipalities_grouped['cobertura_100'] = municipalities_grouped['cobertura_100'].round(2)
	municipalities_grouped['cobertura_3g'] = municipalities_grouped['cobertura_3g'].round(2)
	municipalities_grouped['cobertura_4g'] = municipalities_grouped['cobertura_4g'].round(2)
	
	municipalities_grouped = municipalities_grouped.drop('codigo_esp', axis=1)
	municipalities_grouped.insert(0, 'codigo_ine', municipalities_grouped.pop('codigo_ine'))
	municipalities_grouped.insert(1, 'comunidad_autonoma', municipalities_grouped.pop('comunidad_autonoma'))
	municipalities_grouped.to_csv(new_municipalities_fn)

if __name__ == "__main__":
	main(sys.argv)