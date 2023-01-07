#!/usr/bin/python

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

		text = re.sub(r"\[[0-9]+\]", '', text)

		images = []
		for image in images_urls:
			if "flag" not in image and "coat" not in image and "bandera" not in image and "escudo" not in image and \
				"Flag" not in image and "Coat" not in image and "Bandera" not in image and "Escudo" not in image and \
				"logo" not in image and "icon" not in image and "Logo" not in image and "Icon" not in image and \
				"svg" not in image and "Svg" not in image and "SVG" not in image:
				images.append(image)

		images = images[:10]

	except:
		print("Error con municipio: " + municipality + " (" + province + ")")

	return text, url, images

def get_text(row):
	return row[0]

def get_url(row):
	return row[1]

def get_images(row):
	return row[2]

def sanitize_province(row):
	if row == "Islas Baleares":
		return "Illes Balears"
	else:
		return row

def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 get-wikipedia.py filename.csv')
		sys.exit(2)
	filename = sys.argv[1]
	new_filename = os.path.splitext(filename)[0] + "_wikipedia" + ".json"
	df = pd.read_csv(filename)

	df['text_url_images'] = df.apply(get_wikipedia, axis=1)
	df['text'] = df['text_url_images'].apply(get_text)
	df['url'] = df['text_url_images'].apply(get_url)
	df['images'] = df['text_url_images'].apply(get_images)

	df['provincia'] = df['provincia'].apply(sanitize_province)

	df = df.drop('text_url_images', axis=1)
	df = df.set_index("codigo_ine")
	out = df.to_json(orient = 'index')
	with open(new_filename, 'w') as f:
		f.write(out)

if __name__ == "__main__":
	main(sys.argv)