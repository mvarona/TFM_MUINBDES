#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns the model in CSV

import sys
import os
import pandas as pd
import re

def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 create-model.py filename.csv')
		sys.exit(2)
	filename = sys.argv[1]
	new_filename = "model" + ".csv"
	
	df = pd.read_csv(filename)
	df = df.drop(['municipio', 'provincia', 'municipio_nombre_humano', 'comunidad_autonoma', 'lat', 'lon'], axis=1)

	df = df.replace({'-': 0})

	df.to_csv(new_filename, index=False)

if __name__ == "__main__":
	main(sys.argv)