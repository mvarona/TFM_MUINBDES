#!/usr/bin/python

import sys
import os
import pandas as pd
import re
import numpy as np
import csv
import shutil

def complete_df(incomplete_municipalities, incomplete_fields_fn, new_filename, municipalities, provinces, municipalities_human_names):
	municipalities_to_add = []
	provinces_to_add = []
	municipalities_human_names_to_add = []
	
	i = 0
	for municipality in municipalities:
		if municipality not in incomplete_municipalities:
			municipalities_to_add.append(municipality)
			provinces_to_add.append(provinces[i])
			municipalities_human_names_to_add.append(municipalities_human_names[i])
		i += 1

	prices_to_add = ["-" for i in range(len(municipalities_to_add))]
	num_properties_to_add = ["-" for i in range(len(municipalities_to_add))]

	shutil.copyfile(incomplete_fields_fn, new_filename)

	with open(new_filename,'a') as f:
		i = 0
		for municipality_to_add in municipalities_to_add:
			new_row = municipalities_to_add[i] + "," + provinces_to_add[i] + "," + municipalities_human_names_to_add[i] + "," + prices_to_add[i] + "," + num_properties_to_add[i]	+ "\n"
			f.write(new_row)
			i += 1
		f.close()

def main(argv):
	if (len(sys.argv) < 3):
		print('Uso: python3 get-missing-fields.py filename_with_incomplete_fields.csv filename_with_all_fields.csv')
		sys.exit(2)

	incomplete_fields_fn = sys.argv[1]
	incomplete_fields_df = pd.read_csv(incomplete_fields_fn)
	new_filename = os.path.splitext(incomplete_fields_fn)[0] + "_complete" + ".csv"
	
	reference_fn = sys.argv[2]
	reference_df = pd.read_csv(reference_fn)

	incomplete_municipalities = incomplete_fields_df['municipio'].tolist()
	municipalities = reference_df['municipio'].tolist()
	provinces = reference_df['provincia'].tolist()
	municipalities_human_names = reference_df['municipio_nombre_humano'].tolist()

	complete_df(incomplete_municipalities, incomplete_fields_fn, new_filename, municipalities, provinces, municipalities_human_names)

if __name__ == "__main__":
	main(sys.argv)