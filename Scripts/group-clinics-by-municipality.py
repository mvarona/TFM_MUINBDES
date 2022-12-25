#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with the health clinics group by municipality

import sys
import os
import pandas as pd
import re
import json
import numpy as np

def convert_to_title(row):
	return row.title()

def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 group-clinics-by-municipality.py filename.csv')
		sys.exit(2)
	fn = sys.argv[1]
	new_fn = os.path.splitext(fn)[0] + "_clinics" + ".csv"
	df = pd.read_csv(fn)
	df = df.drop(['Nombre', 'Comunidad Autónoma', 'Localidad', 'Direccion', 'Código Postal', 'Telefono', 'Zona Básica', 'Área de Salud', 'Modalidad Gestión', 'Dependencia de Gestión', 'Tipo de Centro', 'Acreditación Docente'], axis=1)
	
	df['num_centros_salud'] = 1
	df['Provincia'] = df['Provincia'].apply(convert_to_title)
	df_grouped = df.groupby(['Municipio', 'Provincia'])['num_centros_salud'].sum()

	df_grouped.to_csv(new_fn)

if __name__ == "__main__":
	main(sys.argv)