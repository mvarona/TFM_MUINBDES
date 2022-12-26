#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with the two passed files merged

import sys
import os
import pandas as pd
import re
import numpy as np

def main(argv):
	if (len(sys.argv) < 3):
		print('Uso: python3 merge.py filename1.csv filename2.csv')
		sys.exit(2)

	filename1 = sys.argv[1]
	filename2 = sys.argv[2]
	new_filename = os.path.splitext(filename1)[0] + "_merged" + ".csv"
	df1 = pd.read_csv(filename1)
	df2 = pd.read_csv(filename2)

	df2 = df2.drop(["municipio","provincia"], axis=1)
	inner_merged = pd.merge(df1, df2, on="codigo_ine")
	#inner_merged.insert(0, 'codigo_ine', inner_merged.pop('codigo_ine'))
	#inner_merged.insert(3, 'municipio_nombre_humano', inner_merged.pop('municipio_nombre_humano'))
	#inner_merged["num_centros_urgencias"] = inner_merged["num_centros_urgencias"].astype(int)
	inner_merged.to_csv(new_filename, index=False)

if __name__ == "__main__":
	main(sys.argv)