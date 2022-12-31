#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with the province employment data

import sys
import os
import pandas as pd
import re
import json
import requests
import urllib.parse
import numpy as np

def get_activity_province(df_municipalities, df_provinces):
	province = df_municipalities['provincia']
	price = df_provinces[df_provinces['provincia'] == province]['tasa_actividad'].astype(float).values[0]
	return price

def get_unemployment_province(df_municipalities, df_provinces):
	province = df_municipalities['provincia']
	price = df_provinces[df_provinces['provincia'] == province]['tasa_paro'].astype(float).values[0]
	return price

def get_employment_province(df_municipalities, df_provinces):
	province = df_municipalities['provincia']
	price = df_provinces[df_provinces['provincia'] == province]['tasa_empleo'].astype(float).values[0]
	return price

def get_num_jobs(df_municipalities, df_provinces):
	province = df_municipalities['provincia']
	price = df_provinces[df_provinces['provincia'] == province]['num_empleos'].astype(int).values[0]
	return price

def main(argv):
	if (len(sys.argv) < 3):
		print('Uso: python3 add-province-employment-to-municipality.py municipalities.csv provinces_employment.csv')
		sys.exit(2)
	municipalities_fn = sys.argv[1]
	provinces_fn = sys.argv[2]
	new_municipalities_fn = os.path.splitext(municipalities_fn)[0] + "_employment" + ".csv"
	municipalities = pd.read_csv(municipalities_fn)
	provinces = pd.read_csv(provinces_fn)
	
	municipalities['tasa_actividad_provincia'] = municipalities.apply(get_activity_province, axis=1, args=(provinces,))
	municipalities['tasa_paro_provincia'] = municipalities.apply(get_unemployment_province, axis=1, args=(provinces,))
	municipalities['tasa_empleo_provincia'] = municipalities.apply(get_employment_province, axis=1, args=(provinces,))
	municipalities['num_empleos_provincia'] = municipalities.apply(get_num_jobs, axis=1, args=(provinces,))
	
	municipalities.to_csv(new_municipalities_fn, index=False)

if __name__ == "__main__":
	main(sys.argv)