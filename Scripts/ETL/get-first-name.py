#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with the first name of each municipality

import sys
import os
import pandas as pd
import re
from dotenv import load_dotenv
import json
import requests
import urllib.parse

def get_first_name(df):
	municipality = df['municipio_nombre_humano']
	if ("/" in municipality):
		return municipality.split("/")[0]
	else:
		return df['municipio_nombre_humano']

def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 get-first-name.py filename.csv')
		sys.exit(2)
	filename = sys.argv[1]
	new_filename = os.path.splitext(filename)[0] + "_first_name" + ".csv"
	df = pd.read_csv(filename)
	df['municipio_nombre_humano'] = df.apply(get_first_name, axis=1)
	df = df[df.municipio.str.contains('/')]
	df.to_csv(new_filename, index=False)


if __name__ == "__main__":
	main(sys.argv)