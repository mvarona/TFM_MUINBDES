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

def get_m2_sales(df):
	
	municipality = df['municipio'].lower().replace(" ", "-").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
	province = df['provincia'].lower().replace(" ", "-").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
	price_m2 = "-"
	num_properties = 0

	try:

		url = "https://www.idealista.com/venta-viviendas/" + municipality + "-" + province + "/"

		payload={}
		headers = {
		  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
		  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		  'Accept-Language': 'es-es',
		  'Connection': 'keep-alive',
		  'Accept-Encoding': 'gzip, deflate, br',
		  'Host': 'www.idealista.com',
		  'Cookie': 'datadome=.2ABvM6eQ8jU6wlW~.tsd2WKYOe1-yI4tgFQYMNvbU9A4GxMKHf_xuFWnOTcSAWUnGp64AM60.rX_pYIoLO_OPoYR18.Zey8OTChYua9B3JU8d4W8nYnPdwzWfn717Yo; SESSION=c08d7f5cd41fbac0~d1abb91b-0300-4bed-88d5-fee1dc69716f; contactd1abb91b-0300-4bed-88d5-fee1dc69716f="{\'email\':null,\'phone\':null,\'phonePrefix\':null,\'friendEmails\':null,\'name\':null,\'message\':null,\'message2Friends\':null,\'maxNumberContactsAllow\':10,\'defaultMessage\':true}"; cookieSearch-1="/venta-viviendas/' + municipality + "-" + province + '/:1659232666165"; userUUID=baaec429-66be-420d-a45d-d5b91cb7b8cb'
		}

		response = requests.request("GET", url, headers=headers, data=payload)
		content = BeautifulSoup(response.text, 'lxml')

		num_regex = r"[0-9]+"
		num_txt = content.select("h1#h1-container")[0].text.replace(".", "")
		num_properties = re.findall(num_regex, num_txt)[0]

		prices_txt = content.select(".item-price")
		prices = map(clean_price, prices_txt)
		
		m2_txt = content.select(".item-detail")
		m2 = filter(filter_m2, m2_txt)
		m2 = map(clean_m2, m2)

		prices_list = list(prices)
		m2_list = list(m2)

		if len(prices_list) == len(m2_list):
			prices_per_m2 = np.array(prices_list) / np.array(m2_list)
			price_m2 = prices_per_m2.mean()
			price_m2 = str(round(price_m2, 2))
		
	except:
		print("Error en municipio: " + municipality)

	return price_m2, num_properties

def get_price_m2(pair):
	price = pair[0]
	return price

def get_num_properties(pair):
	num = pair[1]
	return num

def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 get-properties-for-sale.py filename.csv')
		sys.exit(2)
	filename = sys.argv[1]
	new_filename = os.path.splitext(filename)[0] + "_properties" + ".csv"
	df = pd.read_csv(filename)

	df['precio_m2_venta_num_casas_venta'] = df.apply(get_m2_sales, axis=1)
	df['precio_m2_venta'] = df['precio_m2_venta_num_casas_venta'].apply(get_price_m2)
	df['num_casas_venta'] = df['precio_m2_venta_num_casas_venta'].apply(get_num_properties)
	df = df.drop('precio_m2_venta_num_casas_venta', axis=1)
	df.to_csv(new_filename, index=False)

if __name__ == "__main__":
	main(sys.argv)