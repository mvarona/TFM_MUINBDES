#!/usr/bin/python

import sys
import os
import pandas as pd
import json
import random

def build_error_response(msg):
	response = {}
	response["status"] = "Error"
	response["message"] = msg
	return response

def build_success_response(data):
	try:
		response = {}
		response["status"] = "Ok"
		response["data"] = data
		return response
	except:
		error = "Error #3, respuesta exitosa mal construida: " + str(data)
		response = build_error_response(error)
		return return_response(response)
		sys.exit(2)
	return response

def return_response(response):
	default_response = {}
	error = "Error #4, respuesta mal construida: " + str(response)
	default_response["status"] = "Error"
	default_response["message"] = error
	try:
		if response["status"] != "Ok" or response["status"] != "Error":
			if response["status"] == "Error" and len(response["message"]) > 0:
				return json.dumps(response)

			elif response["status"] == "Ok" and response["data"] != None:
				return json.dumps(response)

			else:
				return json.dumps(default_response)
		else:
			return json.dumps(default_response)
	except:
		return json.dumps(default_response)

def get_random_municipality(database_fn, wikipedia_fn, onlyWithImages=False):

	if database_fn == None or wikipedia_fn == None or (onlyWithImages != True and onlyWithImages != False):
		error = "Error #1, argumentos incorrectos: " + str(database_fn) + ", " + str(wikipedia_fn) + ", " + str(onlyWithImages)
		response = build_error_response(error)
		return return_response(response)
		sys.exit(2)

	if len(database_fn) == 0 or len(wikipedia_fn) == 0 or (onlyWithImages != True and onlyWithImages != False):
		error = "Error #1, argumentos incorrectos: " + str(database_fn) + ", " + str(wikipedia_fn) + ", " + str(onlyWithImages)
		response = build_error_response(error)
		return return_response(response)
		sys.exit(2)

	searchRandom = True
	while searchRandom:

		if database_fn and wikipedia_fn:
			try:
				with open(database_fn, 'r') as f:
					database = json.load(f)

				with open(wikipedia_fn, 'r') as f:
					wikipedia_db = json.load(f)

			except:
				error = "Error #2, imposible cargar las bases de datos: " + str(database_fn) + ", " + str(wikipedia_fn)
				response = build_error_response(error)
				return return_response(response)
				sys.exit(2)

			municipalities = list(database.keys())
			nsi_code = random.choice(municipalities)
			municipality = database[nsi_code]
			wikipedia = wikipedia_db[nsi_code]
			result = {}
			result["codigo_ine"] = nsi_code
			result.update(municipality)
			result.update(wikipedia)
			response = build_success_response(result)
			return return_response(response)

			if onlyWithImages:
				searchRandom = len(wikipedia["images"]) == 0
			else:
				searchRandom = False