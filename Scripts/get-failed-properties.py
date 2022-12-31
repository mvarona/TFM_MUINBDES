#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with the properties data that were missing on previous attempts

import sys
import os
import pandas as pd
import re
from dotenv import load_dotenv
import json
import requests
import urllib.parse

def get_clean_name(df):
	municipality = df['municipio_nombre_humano']
	if ("/" in municipality):
		return municipality.split("/")[0]
	else:
		return df['municipio_nombre_humano']

def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 get-error-properties.py filename.csv')
		sys.exit(2)
	filename = sys.argv[1]
	new_filename = os.path.splitext(filename)[0] + "_failed" + ".csv"
	df = pd.read_csv(filename)
	df = df[df['precio_m2_venta'] == "-"]
	df = df[~df.municipio.str.contains('/')]
	df.to_csv(new_filename, index=False)

if __name__ == "__main__":
	main(sys.argv)