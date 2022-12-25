#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with the municipalities associated to a list of singular entities of population

import sys
import os
import pandas as pd
import re
from dotenv import load_dotenv
import json
import requests
import urllib.parse

def get_municipality(df, entities, municipalities):
	name = df['municipio']

	if name not in entities:
		return name
	else:
		i = 0
		for entity in entities:
			if entity == name:
				return municipalities[i]
			i += 1

	return name

def main(argv):
	if (len(sys.argv) < 3):
		print('Uso: python3 get-municipality-from-singular-entity.py filename.csv entities.csv')
		sys.exit(2)
	filename = sys.argv[1]
	new_filename = os.path.splitext(filename)[0] + "_municipalities" + ".csv"
	df = pd.read_csv(filename)
	filename_entities = sys.argv[2]
	df_entities = pd.read_csv(filename_entities)
	entities = df_entities['entidad_nombre_humano'].tolist()
	municipalities = df_entities['municipio_nombre_humano'].tolist()
	df['municipio'] = df.apply(get_municipality, axis=1, args=(entities,municipalities, ))
	df.to_csv(new_filename, index=False)

if __name__ == "__main__":
	main(sys.argv)