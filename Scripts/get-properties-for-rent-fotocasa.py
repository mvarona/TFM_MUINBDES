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

def get_m2_rent(df):
	
	municipality = df['municipio_nombre_humano'].lower().replace("-", " ").replace(" ", "-").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ñ", "n").replace("à", "a").replace("è", "e").replace("ì", "i").replace("ò", "o").replace("ù", "u").replace("ü", "u").replace("ï", "i")
	if "/" in municipality:
		municipality = municipality.split("/")[1]
	province = df['provincia'].lower().replace("-", " ").replace(" ", "-").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ñ", "n").replace("à", "a").replace("è", "e").replace("ì", "i").replace("ò", "o").replace("ù", "u").replace("ü", "u").replace("ï", "i")
	price_m2 = "-"
	num_properties = 0

	try:

		url = "https://www.fotocasa.es/es/alquiler/viviendas/" + municipality + "/todas-las-zonas/l"
		
		response = requests.request("GET", url)
		content = BeautifulSoup(response.text, 'lxml')

		num_regex = r"[0-9]+"
		num_txt = content.select(".re-SearchTitle-count")[0].text.replace(".", "")
		 
		num_properties = re.findall(num_regex, num_txt)[0]

		prices_txt = content.select(".re-CardPrice")

		prices = map(clean_price, prices_txt)
		
		m2_txt = content.select(".re-CardFeatures-feature")
		if len(m2_txt) == 0:
			m2_txt = content.select(".re-CardFeaturesWithIcons-feature-icon--surface")

		m2 = filter(filter_m2, m2_txt)
		m2 = map(clean_m2, m2)

		prices_list = list(prices)
		m2_list = list(m2)

		if len(prices_list) == len(m2_list):
			prices_per_m2 = np.array(prices_list) / np.array(m2_list)
			price_m2 = prices_per_m2.mean()
			price_m2 = str(round(price_m2, 2))

		if len(prices_list) < len(m2_list):
			len_prices = len(prices_list)
			m2_list = m2_list[:len_prices]
			prices_per_m2 = np.array(prices_list) / np.array(m2_list)
			price_m2 = prices_per_m2.mean()
			price_m2 = str(round(price_m2, 2))

		if len(prices_list) > len(m2_list):
			len_m2 = len(m2_list)
			prices_list = prices_list[:len_m2]
			prices_per_m2 = np.array(prices_list) / np.array(m2_list)
			price_m2 = prices_per_m2.mean()
			price_m2 = str(round(price_m2, 2))
			
			
			time.sleep(1)
		
	except:
		print("Error en municipio: " + df['municipio_nombre_humano'] + " (" + municipality + ")")

	return price_m2, num_properties

def get_price_m2(pair):
	price = pair[0]
	return price

def get_num_properties(pair):
	num = pair[1]
	return num

def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 get-properties-for-rent-fotocasa.py filename.csv')
		sys.exit(2)
	filename = sys.argv[1]
	new_filename = os.path.splitext(filename)[0] + "_properties_4" + ".csv"
	df = pd.read_csv(filename)

	df['precio_m2_alquiler_num_casas_alquiler'] = df.apply(get_m2_rent, axis=1)
	df['precio_m2_alquiler'] = df['precio_m2_alquiler_num_casas_alquiler'].apply(get_price_m2)
	df['num_casas_alquiler'] = df['precio_m2_alquiler_num_casas_alquiler'].apply(get_num_properties)
	df = df.drop('precio_m2_alquiler_num_casas_alquiler', axis=1)
	df.to_csv(new_filename, index=False)

if __name__ == "__main__":
	main(sys.argv)