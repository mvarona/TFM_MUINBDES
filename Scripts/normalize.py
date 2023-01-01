#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns the model Ridge-normalized on CSV

import pandas as pd
import sys
import os
import pandas as pd
import re
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import Ridge, LinearRegression

def main(argv):
	if (len(sys.argv) < 2):
		print('Uso: python3 normalize.py model.csv')
		sys.exit(2)
	model_fn = sys.argv[1]
	new_model_fn = os.path.splitext(model_fn)[0] + "_normalized" + ".csv"
	model = pd.read_csv(model_fn)
	
	model = model.reset_index(drop=True)
	target = model[['poblacion']]
	target = MinMaxScaler().fit_transform(target)

	predictors = model.drop(['codigo_ine', 'poblacion'], axis=1)
	X = MinMaxScaler().fit_transform(predictors)
	reg = Ridge().fit(X, target)
	score = reg.score(X, target)
	xxx = [i for i in reg.coef_]
	X = X * xxx
	
	norm_df = pd.DataFrame(X)
	columns = list(predictors.columns)
	names_norm = {}

	for i in range(0, len(columns)):
	    names_norm[i] = columns[i]
	    
	norm_df = norm_df.rename(columns=names_norm)
	norm_df.insert(0, 'codigo_ine', model.codigo_ine)

	norm_df.to_csv(new_model_fn, index=False)

if __name__ == "__main__":
	main(sys.argv)