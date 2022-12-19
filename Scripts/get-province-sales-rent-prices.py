#!/usr/bin/python

from bs4 import BeautifulSoup
import sys
import os
import pandas as pd
import re
import json
import requests
import urllib.parse
import numpy as np
import time

def clean_price(price_txt):
	num_regex = r"[0-9]+"
	price = re.findall(num_regex, price_txt.text.replace(".", ""))[0]
	return int(price)

def filter_m2(m2_txt):
	m2_regex = r"[0-9]+ m"
	if len(re.findall(m2_regex, m2_txt.text)) > 0:
		return True
	return False

def clean_m2(m2_txt):
	m2_regex = r"[0-9]+ m"
	m2 = re.findall(m2_regex, m2_txt.text)[0].replace(" m", "")
	return int(m2)

def get_m2_sales_rent(df):
	
	province = df['provincia'].lower().replace("-", " ").replace(" ", "-").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ñ", "n").replace("à", "a").replace("è", "e").replace("ì", "i").replace("ò", "o").replace("ù", "u").replace("ü", "u").replace("ï", "i")
	price_m2_sales = "-"
	avg_sales = "-"
	price_m2_rent = "-"
	avg_rent = "-"

	try:

		url = "https://www.fotocasa.es/indice-precio-vivienda/" + province + "-provincia/todas-las-zonas"

		response = requests.request("GET", url)
		content = BeautifulSoup(response.text, 'lxml')

		num_regex = r"[0-9]+"
		nums_txt = content.select(".b-detail_title")
		
		price_m2_sales = nums_txt[0].text.replace(".", "")
		price_m2_sales = re.findall(num_regex, price_m2_sales)[0]

		avg_sales = nums_txt[1].text.replace(".", "")
		avg_sales = re.findall(num_regex, avg_sales)[0]

		price_m2_rent = nums_txt[2].text.replace(".", "")
		price_m2_rent = re.findall(num_regex, price_m2_rent)[0]

		avg_rent = nums_txt[3].text.replace(".", "")
		avg_rent = re.findall(num_regex, avg_rent)[0]

		time.sleep(2)
		
	except:
		print("Error en municipio: " + df['provincia'] + " (" + province + ")")

	return price_m2_sales, avg_sales, price_m2_rent, avg_rent

def get_price_m2_sales(group):
	price = group[0]
	return price

def get_avg_sales(group):
	price = group[1]
	return price

def get_price_m2_rent(group):
	price = group[2]
	return price

def get_avg_rent(group):
	price = group[3]
	return price

def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 get-province-sales-rent-prices.py filename.csv')
		sys.exit(2)
	filename = sys.argv[1]
	new_filename = os.path.splitext(filename)[0] + "_prices" + ".csv"
	df = pd.read_csv(filename)

	df['precio_m2_venta_alquiler'] = df.apply(get_m2_sales_rent, axis=1)
	df['precio_m2_venta'] = df['precio_m2_venta_alquiler'].apply(get_price_m2_sales)
	df['precio_medio_venta'] = df['precio_m2_venta_alquiler'].apply(get_avg_sales)
	df['precio_m2_alquiler'] = df['precio_m2_venta_alquiler'].apply(get_price_m2_rent)
	df['precio_medio_alquiler'] = df['precio_m2_venta_alquiler'].apply(get_avg_rent)
	df = df.drop('precio_m2_venta_alquiler', axis=1)
	df.to_csv(new_filename, index=False)

if __name__ == "__main__":
	main(sys.argv)