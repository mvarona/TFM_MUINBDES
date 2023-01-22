#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with the recommendations of the content-based recommender

import pandas as pd
import sys
import os
import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json

def cosine_similarity_for_nsi_code(data, nsi_code):
	nsi_code = int(nsi_code)

	try:
		Xs = data[data.codigo_ine == nsi_code].drop('codigo_ine', axis=1)
		col_codigo_ine = data[data.codigo_ine != nsi_code].codigo_ine
		Ys = data[data.codigo_ine != nsi_code].drop('codigo_ine', axis=1)
		cos_sim = cosine_similarity(X=Xs, Y=Ys)
		sim = list(cos_sim[0])
		codes = list(col_codigo_ine)
		comb = { "codigo_ine": codes, "similitud": sim }
		dfdf = pd.DataFrame(comb).reset_index()
		
		current_nsi_code = { "codigo_ine": nsi_code, "similitud":1 }
		current = pd.DataFrame(current_nsi_code, index=[0])
		dfdf = pd.concat([dfdf, current], sort=False).reset_index(drop=True).drop('index', axis=1)
		
		return(dfdf)
	
	except:
		error = "Error #4 en municipio con codigo INE: " + str(nsi_code)
		response = build_error_response(error)
		return return_response(response)
		sys.exit(2)

def return_response(response):
	default_response = {}
	error = "Error #2, respuesta mal construida: " + str(response)
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

def build_error_response(msg):
	response = {}
	response["status"] = "Error"
	response["message"] = msg
	return response

def complete_nsi_code(row):
	code = row
	if code < 1000:
		code = "00" + str(row)

	if code < 10000:
		code = "0" + str(row)

	return code

def build_success_response(data):
	try:
		response = {}
		response["status"] = "Ok"
		data['codigo_ine'] = data['codigo_ine'].apply(complete_nsi_code)
		response["data"] = data.set_index('codigo_ine').T.to_dict('records')[0]
	
	except:
		error = "Error #5, respuesta exitosa mal construida: " + str(data)
		response = build_error_response(error)
		return return_response(response)
		sys.exit(2)
	return response

def check_nsi_code_integrity(nsi_code):
	if len(nsi_code) == 5:
		try:
			nsi_code_int = int(nsi_code)
			return nsi_code_int
		except:
			error = "Error #3, codigo INE con formato incorrecto: " + nsi_code
			response = build_error_response(error)
			return return_response(response)
			sys.exit(2)
	else:
		error = "Error #2, codigo INE de longitud no valida: " + nsi_code
		response = build_error_response(error)
		return return_response(response)
		sys.exit(2)

def recommend(input_code):
	model_fn = "model_normalized.csv"
	model = pd.read_csv(model_fn)
	nsi_code = check_nsi_code_integrity(input_code)

	results = cosine_similarity_for_nsi_code(model, nsi_code).nlargest(columns='similitud', n=11)
	response = build_success_response(results)
	return return_response(response)