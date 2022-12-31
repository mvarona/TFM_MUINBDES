#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with properties merged data

import sys
import os
import pandas as pd
import re
from dotenv import load_dotenv
import json
import requests
import urllib.parse
import numpy as np

def set_nan_price(df):
	if df['precio_m2_venta'] == '-' and df['num_casas_venta'] == 0:
		return np.nan
	return df['precio_m2_venta']

def set_nan_num(df):
	if pd.isna(df['precio_m2_venta']) and df['num_casas_venta'] == 0:
		return np.nan
	return df['num_casas_venta']

def main(argv):
	if (len(sys.argv) < 3):
		print('Uso: python3 merge-properties.py filename1.csv filename2.csv')
		sys.exit(2)
	filename1 = sys.argv[1]
	filename2 = sys.argv[2]
	new_filename = os.path.splitext(filename1)[0] + "_merged" + ".csv"
	df1 = pd.read_csv(filename1)
	df2 = pd.read_csv(filename2)
	df1['precio_m2_venta'] = df1.apply(set_nan_price, axis=1)
	df1['num_casas_venta'] = df1.apply(set_nan_num, axis=1)
	df1 = df1.dropna(subset=['precio_m2_venta', 'num_casas_venta'], how='any')
	df = pd.concat([df1, df2])
	df.to_csv(new_filename, index=False)


if __name__ == "__main__":
	main(sys.argv)