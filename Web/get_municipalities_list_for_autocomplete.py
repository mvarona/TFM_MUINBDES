#!/usr/bin/python

import sys
import os
import json
import random

def get_municipalities_list_for_autocomplete():
	
	with open("database.json", 'r') as f:
		database = json.load(f)
	
	municipalities_names = []
	municipalities_codes = []
	for code in database:
		municipalities_names.append(database[code]["municipio_nombre_humano"] + ", " + database[code]["provincia"])
		municipalities_codes.append(code)

	names = "var municipalitiesNames = " + str(municipalities_names) + ";\n"
	codes = "var municipalitiesCodes = " + str(municipalities_codes) + ";\n"

	text = names + codes

	with open("static/js/municipalities.js", "w+") as f:
		f.write(text)

get_municipalities_list_for_autocomplete()