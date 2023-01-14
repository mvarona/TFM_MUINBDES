#!/usr/bin/python

import pandas as pd
from io import StringIO
import recommender
import json
import requests

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