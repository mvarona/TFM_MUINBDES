#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with the schools grouped by municipality, and their sum

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
		print('Uso: python3 group-schools-by-municipality.py filename.csv')
		sys.exit(2)
	fn = sys.argv[1]
	new_fn = os.path.splitext(fn)[0] + "_sum" + ".csv"
	df = pd.read_csv(fn)
	
	df_grouped = df.groupby(['municipio'])['num_colegios'].sum()

	df_grouped.to_csv(new_fn)

if __name__ == "__main__":
	main(sys.argv)