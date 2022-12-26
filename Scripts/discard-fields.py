#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with the specified fields (columns) removed

import sys
import os
import pandas as pd
import re
import numpy as np

def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 discard-fields.py filename1.csv')
		sys.exit(2)

	filename1 = sys.argv[1]
	new_filename = os.path.splitext(filename1)[0] + "_discarded" + ".csv"
	df1 = pd.read_csv(filename1)
	
	df1 = df1.drop(["titulares","numero_declaraciones","numero_habitantes","posicionamiento_renta_bruta_media_nivel_nacional","posicionamiento_renta_bruta_media_nivel_autonomico","renta_disponible_media"], axis=1)
	df1.to_csv(new_filename, index=False)

if __name__ == "__main__":
	main(sys.argv)