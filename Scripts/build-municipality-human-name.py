#!/usr/bin/python

import sys
import os
import pandas as pd
import re

def build_human_friendly_name(row):
	regex_parenthesis = r" \([A-z]+\)| \([A-z]+'\)"

	if (len(re.findall(regex_parenthesis, row)) > 0):
		prefix_with_parenthesis = re.findall(regex_parenthesis, row)[0]
		new_row = row.replace(prefix_with_parenthesis, "")
		prefix = prefix_with_parenthesis.replace("(", "").replace(")", "").strip().capitalize()
		new_row = prefix + " " + new_row

		return new_row
	else:
		return row


def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 build-municipality-human-name.py filename.csv')
		sys.exit(2)
	filename = sys.argv[1]
	new_filename = os.path.splitext(filename)[0] + "_nombres_humanos" + ".csv"
	df = pd.read_csv(filename)
	df['municipio_nombre_humano'] = df['municipio']
	df['municipio_nombre_humano'] = df['municipio_nombre_humano'].apply(build_human_friendly_name)
	df.to_csv(new_filename, index=False)


if __name__ == "__main__":
	main(sys.argv)