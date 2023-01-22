#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2023
# Returns a CSV with the recommendations of the collaborative filter based on items

import pandas as pd
from io import StringIO
import recommender
import json
import requests
import numpy as np
from copy import deepcopy
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
from collections import OrderedDict
from operator import itemgetter  

def generate_suggestions(ratings, auth_token):
	
	df = pd.read_csv(StringIO(ratings))
	
	likes = df[df['rating']==1]
	users = likes['user']
	suggestions = {}

	for user in users:
		user_likes = likes[likes['user']==user]['item']
		suggestions[user] = []
		for user_like in user_likes:
			result = json.loads(recommender.recommend(str(user_like)))
			if result["status"] == "Ok":
				top_suggestions = list(result['data'].keys())[1:6]
				suggestions[user].extend(top_suggestions)

	codes = pd.read_csv("model_normalized.csv")['codigo_ine'].tolist()	
	utility = df.pivot(index = 'item', columns = 'user', values = 'rating')
	utility = utility.reindex(codes, fill_value=0.5).reset_index()
	utility['item'] = utility['item'].apply(complete_nsi_code)
	utility = utility.set_index('item')
	utility = utility.fillna(0.5)

	distance_mtx = squareform(pdist(utility, 'cosine'))
	similarity_mtx = 1 - distance_mtx
	similarity_mtx[np.isnan(similarity_mtx)] = 0.5

	users_filter = df['user'].unique()
	users_recommendations = {}
	num_users = 0
	num_municipities = 0

	for user in users_filter:
		users_recommendations[user] = {}
		for municipality in codes:
			res = compute_prediction(num_users, num_municipities, similarity_mtx, utility)
			users_recommendations[user][municipality] = res
			num_municipities += 1
		num_users += 1
		num_municipities = 0

	for user in users_recommendations:
		filter_suggestions = OrderedDict(sorted(users_recommendations[user].items(), key = itemgetter(1), reverse = True))
		filter_suggestions = list(filter_suggestions.keys())
		for suggestion in filter_suggestions:
			user_likes = likes[likes['user']==user]['item']
			if suggestion not in user_likes and users_recommendations[user][suggestion] > 0.7:
				suggestions[user].append(complete_nsi_code(suggestion))

	url = "https://www.bmsalamanca.com/others/dondeteesperan/api/update-suggestions"
	params = {
		"auth_token": auth_token,
		"suggestions": json.dumps(suggestions)
	}
	response = requests.post(url, data=params)

	if response.status_code == 200:
		return "Ok"
	else:
		raise

def complete_nsi_code(row):
	code = row
	if code < 1000:
		code = "00" + str(row)

	if code < 10000:
		code = "0" + str(row)

	return code

def compute_prediction(user, item, similarity, utility):
	user_ratings = utility.iloc[:,user]
	item_similarity = similarity[item]

	numerator = np.dot(user_ratings,item_similarity)
	denom = item_similarity[user_ratings > 0].sum()

	if denom != 0:
		prediction = numerator / denom
	else:
		prediction = 0

	return prediction