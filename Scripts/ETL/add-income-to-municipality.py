#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with the province income for municipalities that are too small to have it published

import sys
import os
import pandas as pd
import re
import numpy as np

def get_income(df_municipalities, df_incomes):
	province = df_municipalities['provincia']
	if df_municipalities['renta_bruta_media'] == "-":
		try:
			income = df_incomes[df_incomes['provincia'] == province]['renta_bruta_media'].astype(int).values[0]
		except:
			income = "-"
		return income
	return df_municipalities['renta_bruta_media']

def main(argv):
	if (len(sys.argv) < 3):
		print('Uso: python3 add-income-to-municipality.py municipalities.csv income_per_province.csv')
		sys.exit(2)
	municipalities_fn = sys.argv[1]
	incomes_fn = sys.argv[2]
	new_municipalities_fn = os.path.splitext(municipalities_fn)[0] + "_incomes" + ".csv"
	municipalities = pd.read_csv(municipalities_fn)
	incomes = pd.read_csv(incomes_fn)
	
	municipalities['renta_bruta_media'] = municipalities.apply(get_income, axis=1, args=(incomes, ))
	
	municipalities.to_csv(new_municipalities_fn, index=False)

if __name__ == "__main__":
	main(sys.argv)