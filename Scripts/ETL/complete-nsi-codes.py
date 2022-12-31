#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns the same CSV but filling the NSI codes with leading zeroes in case they have been lost

import sys
import os
import pandas as pd
import re
import json
import requests
import urllib.parse
import numpy as np

def complete_nsi_code(row):
	code = row
	if code < 1000:
		code = "00" + str(row)

	if code < 10000:
		code = "0" + str(row)

	return code

def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 complete-nsi-codes.py filename.csv')
		sys.exit(2)
	df_fn = sys.argv[1]
	df = pd.read_csv(df_fn)
	
	columns = list(df)

	if 'codigo_ine' in columns:
		df['codigo_ine'] = df['codigo_ine'].apply(complete_nsi_code)
		df.to_csv(df_fn, index=False)

if __name__ == "__main__":
	main(sys.argv)