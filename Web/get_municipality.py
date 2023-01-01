#!/usr/bin/python

import sys
import os
import pandas as pd
import json

def get_municipality_info(nsi_code):
	with open("database.json", 'r') as f:
		database = json.load(f)[nsi_code]
	with open("wikipedia.json", 'r') as f:
		wikipedia = json.load(f)[nsi_code]

	response = {}
	response["codigo_ine"] = nsi_code
	response["data"] = {}
	response["data"].update(database)
	response["data"].update(wikipedia)

	return response