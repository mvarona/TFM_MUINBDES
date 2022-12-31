#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with the coast and mountain line of each municipality

import sys
import os
import pandas as pd
import re
import json
import requests
import urllib.parse
import numpy as np
import time

def get_coast_line(df_municipalities, df_provinces):
	province = df_municipalities['provincia']
	line = df_provinces[df_provinces['provincia'] == province]['linea_playa'].astype(int).values[0]
	return line

def get_montain_line(df_municipalities, df_provinces):
	province = df_municipalities['provincia']
	line = df_provinces[df_provinces['provincia'] == province]['linea_montana'].astype(int).values[0]
	return line

def main(argv):
	if (len(sys.argv) < 3):
		print('Uso: python3 add-coast-mountain-to-municipality.py municipalities.csv coast_mountain.csv')
		sys.exit(2)
	municipalities_fn = sys.argv[1]
	coast_mountain_fn = sys.argv[2]
	new_municipalities_fn = os.path.splitext(municipalities_fn)[0] + "_province_lines" + ".csv"
	municipalities = pd.read_csv(municipalities_fn)
	coast_mountain = pd.read_csv(coast_mountain_fn)
	
	municipalities['linea_costa_provincia'] = municipalities.apply(get_coast_line, axis=1, args=(coast_mountain, ))
	municipalities['linea_montana_provincia'] = municipalities.apply(get_montain_line, axis=1, args=(coast_mountain, ))
	
	municipalities.to_csv(new_municipalities_fn, index=False)

if __name__ == "__main__":
	main(sys.argv)