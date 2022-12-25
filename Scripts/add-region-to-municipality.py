#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with the region of each municipality

import sys
import os
import pandas as pd
import re
import json
import requests
import urllib.parse
import numpy as np
import time

def get_region(df_municipalities, df_regions):
	province = df_municipalities['provincia']
	region = df_regions[df_regions['provincia'] == province]['comunidad_autonoma'].astype(str).values[0]
	return region

def main(argv):
	if (len(sys.argv) < 3):
		print('Uso: python3 add-region-to-municipality.py municipalities.csv regions.csv')
		sys.exit(2)
	municipalities_fn = sys.argv[1]
	regions_fn = sys.argv[2]
	new_municipalities_fn = os.path.splitext(municipalities_fn)[0] + "_regions" + ".csv"
	municipalities = pd.read_csv(municipalities_fn)
	regions = pd.read_csv(regions_fn)
	
	municipalities['comunidad_autonoma'] = municipalities.apply(get_region, axis=1, args=(regions, ))
	
	municipalities.to_csv(new_municipalities_fn, index=False)

if __name__ == "__main__":
	main(sys.argv)