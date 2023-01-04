#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with the correct incomes per person (and not per family) for the Basque Country

import sys
import os
import pandas as pd
import re

def update_incomes(df, new, nsi_codes_to_change):

	if df["codigo_ine"] in nsi_codes_to_change:
		return new[new["codigo_ine"] == df["codigo_ine"]]["renta_bruta_media_corregida"].astype(int).values[0]
	else:
		return df["renta_bruta_media"]

def complete_nsi_code(code):
	code = str(code)
	if len(code) == 4:
		return "0" + code
	return code

def main(argv):
	if (len(sys.argv) < 3):
		print('Uso: python3 fix-incomes.py database.csv changes_incomes.csv')
		sys.exit(2)
	filename = sys.argv[1]
	changes_fn = sys.argv[2]
	new_filename = os.path.splitext(filename)[0] + "_incomes_fixed" + ".csv"
	df = pd.read_csv(filename)
	new = pd.read_csv(changes_fn)


	nsi_codes_to_change = new['codigo_ine'].tolist()

	print(len(df['renta_bruta_media']))
	print(df['renta_bruta_media'])
	print(len(df[df['comunidad_autonoma'] == "País Vasco"]))
	print(df[df['comunidad_autonoma'] == "País Vasco"]["renta_bruta_media"])
	
	df['renta_bruta_media'] = df.apply(update_incomes, axis=1, args=(new, nsi_codes_to_change, ))
	
	print(len(df['renta_bruta_media']))
	print(len(df[df['comunidad_autonoma'] == "País Vasco"]))
	print(df[df['comunidad_autonoma'] == "País Vasco"]["renta_bruta_media"])


	df.to_csv(new_filename, index=False)

if __name__ == "__main__":
	main(sys.argv)