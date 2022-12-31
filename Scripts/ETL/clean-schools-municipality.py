#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Removes rows belonging to singular entities of population

import sys
import os
import pandas as pd
import re

def clean_school(df, municipalities):
	if df['municipio'] not in municipalities:
		return "-","-"
	return df['municipio'], df['num_colegios']

def get_municipality(row):
	return row[0]

def get_num_schools(row):
	return row[1]

def main(argv):
	if (len(sys.argv) < 3):
		print('Uso: python3 clean-schools-municipality.py filename.csv filename2.csv')
		sys.exit(2)
	filename = sys.argv[1]
	new_filename = os.path.splitext(filename)[0] + "_clean" + ".csv"
	reference_fn = sys.argv[2]
	df = pd.read_csv(filename)
	reference_df = pd.read_csv(reference_fn)
	municipalities = reference_df['municipio_nombre_humano'].tolist()

	df['new_municipio_new_num'] = df.apply(clean_school, axis=1, args=(municipalities, ))
	df['municipio_nombre_humano'] = df['new_municipio_new_num'].apply(get_municipality)
	df['num_colegios_'] = df['new_municipio_new_num'].apply(get_num_schools)
	df = df.drop(['new_municipio_new_num', 'num_colegios', 'municipio'], axis=1)
	df.to_csv(new_filename, index=False)

if __name__ == "__main__":
	main(sys.argv)