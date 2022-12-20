#!/usr/bin/python

import sys
import os
import pandas as pd
import re
import json
import requests
import urllib.parse
import numpy as np
import time

def get_price_m2_sales(df_municipalities, df_provinces):
	province = df_municipalities['provincia']
	price = df_provinces[df_provinces['provincia'] == province]['precio_m2_venta'].astype(float).values[0]
	return price

def get_avg_sales(df_municipalities, df_provinces):
	province = df_municipalities['provincia']
	price = df_provinces[df_provinces['provincia'] == province]['precio_medio_venta'].astype(int).values[0]
	return price

def get_price_m2_rent(df_municipalities, df_provinces):
	province = df_municipalities['provincia']
	price = df_provinces[df_provinces['provincia'] == province]['precio_m2_alquiler'].astype(float).values[0]
	return price

def get_avg_rent(df_municipalities, df_provinces):
	province = df_municipalities['provincia']
	price = df_provinces[df_provinces['provincia'] == province]['precio_medio_alquiler'].astype(int).values[0]
	return price

def main(argv):
	if (len(sys.argv) < 3):
		print('Uso: python3 add-province-prices-to-municipality.py municipalities.csv provinces_prices.csv')
		sys.exit(2)
	municipalities_fn = sys.argv[1]
	provinces_fn = sys.argv[2]
	new_municipalities_fn = os.path.splitext(municipalities_fn)[0] + "_prices" + ".csv"
	municipalities = pd.read_csv(municipalities_fn)
	provinces = pd.read_csv(provinces_fn)
	
	municipalities['precio_m2_venta_provincia'] = municipalities.apply(get_price_m2_sales, axis=1, args=(provinces, ))
	municipalities['precio_medio_venta_provincia'] = municipalities.apply(get_avg_sales, axis=1, args=(provinces, ))
	municipalities['precio_m2_alquiler_provincia'] = municipalities.apply(get_price_m2_rent, axis=1, args=(provinces, ))
	municipalities['precio_medio_alquiler_provincia'] = municipalities.apply(get_avg_rent, axis=1, args=(provinces, ))
	
	municipalities.to_csv(new_municipalities_fn, index=False)

if __name__ == "__main__":
	main(sys.argv)