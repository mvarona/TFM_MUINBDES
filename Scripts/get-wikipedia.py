#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with the summary of the Wikipedia page for the municipality and its main photos

import sys
import os
import pandas as pd
import re
import wikipedia

def get_wikipedia(df):
	municipality = df['municipio_nombre_humano']
	province = df['provincia']
	terms = municipality + ", " + province
	text = ""
	url = ""
	images = ""
	try:
		wikipedia.set_lang("es")
		result = wikipedia.search(terms)[0]
		page = wikipedia.page(result)
		text = page.summary
		url = page.url
		images_urls = page.images

		text = ""
		sentences = page.summary.split(".")
		num_regex = r"[0-9]+"
		for sentence in sentences:
			if len(sentence) > 1:
				if len(re.findall(num_regex, sentence)) == 0:
					text += sentence + "."

		images = []
		for image in images_urls:
			if "flag" not in image and "coat" not in image and "bandera" not in image and "escudo" not in image and \
				"Flag" not in image and "Coat" not in image and "Bandera" not in image and "Escudo" not in image and \
				"logo" not in image and "icon" not in image and "Logo" not in image and "Icon" not in image and \
				"svg" not in image and "Svg" not in image and "SVG" not in image:
				images.append(image)

	except:
		print("Error con municipio: " + municipality + " (" + province + ")")

	return text, url, images

def get_text(row):
	return row[0]

def get_url(row):
	return row[1]

def get_images(row):
	return row[2]

def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 get-wikipedia.py filename.csv')
		sys.exit(2)
	filename = sys.argv[1]
	new_filename = os.path.splitext(filename)[0] + "_wikipedia" + ".csv"
	df = pd.read_csv(filename)

	df['text_url_images'] = df.apply(get_wikipedia, axis=1)
	df['text'] = df['text_url_images'].apply(get_text)
	df['url'] = df['text_url_images'].apply(get_url)
	df['images'] = df['text_url_images'].apply(get_images)

	df = df.drop('text_url_images', axis=1)
	df.to_csv(new_filename, index=False)

if __name__ == "__main__":
	main(sys.argv)