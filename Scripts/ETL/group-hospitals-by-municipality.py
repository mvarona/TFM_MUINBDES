#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with the hospitals grouped by municipality and province, and their sum

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
		print('Uso: python3 group-hospitals-by-municipality.py filename.csv')
		sys.exit(2)
	fn = sys.argv[1]
	new_fn = os.path.splitext(fn)[0] + "_hospitals" + ".csv"
	df = pd.read_csv(fn)
	df = df.drop(['Código CCN','Código CNH','Nombre','Comunidad Autónoma','Dirección','Código Postal','Teléfono','Número de camas instaladas','Tipo de Centro','Dependencia Funcional','Observaciones','Concierto','Acreditación Docente'], axis=1)
	
	df['num_hospitals'] = 1
	df['Provincia'] = df['Provincia'].apply(convert_to_title)
	df_grouped = df.groupby(['Municipio', 'Provincia'])['num_hospitals'].sum()

	df_grouped.to_csv(new_fn)

if __name__ == "__main__":
	main(sys.argv)