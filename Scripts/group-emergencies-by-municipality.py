#!/usr/bin/python

import sys
import os
import pandas as pd
import re
import json
import numpy as np

def convert_to_title(row):
	return row.title()

def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 group-emergencies-by-municipality.py filename.csv')
		sys.exit(2)
	fn = sys.argv[1]
	new_fn = os.path.splitext(fn)[0] + "_emergencies" + ".csv"
	df = pd.read_csv(fn)
	df = df.drop(['Localidad', 'Nombre', 'Ubicación'], axis=1)
	
	df['tiene_urgencias'] = 1
	df['Provincia'] = df['Provincia'].apply(convert_to_title)
	df_grouped = df.groupby(['Municipio', 'Provincia'])['tiene_urgencias'].count()

	df_grouped.to_csv(new_fn)

if __name__ == "__main__":
	main(sys.argv)