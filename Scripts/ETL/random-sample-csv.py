#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with a sample of the data

import sys
import random
import os
import pandas as pd

def sample_n_from_csv(filename:str, n:int=100) -> pd.DataFrame:
	total_rows = 0
	with open(filename,"r") as fh:
		total_rows = sum(1 for row in fh)

	if (n > total_rows):
		print("Error: n > total_rows", file=sys.stderr) 
		return

	skip_rows =  random.sample(range(1, total_rows+1), total_rows-n)
	mini_filename = os.path.splitext(filename)[0] + "-mini" + ".csv"

	return pd.read_csv(filename, skiprows=skip_rows).to_csv(mini_filename, index=False)

def main(argv):
	if (len(sys.argv) < 3):
		print('Uso: python3 random-sample-csv.py filename.csv num_rows_to_sample')
		sys.exit(2)
	sample_n_from_csv(sys.argv[1], int(sys.argv[2]))

if __name__ == "__main__":
	main(sys.argv)