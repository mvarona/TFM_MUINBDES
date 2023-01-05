import pandas as pd
import random
import string
import time
import datetime

def commit_rating(user, item, rating):
	user_length = 32
	item_length = 5

	if len(user) == user_length and len(item) == item_length:

		df = pd.read_csv("ratings.csv")
		df['item'] = df['item'].astype(str)
		df = df.set_index(["item", "user"])

		try:
			df.loc[item, user]["rating"] = rating
		except:
			print("HERE")
			new_rating = pd.DataFrame({
				"item":[item],
				"user":[user],
				"rating":[rating]
			})
			new_rating['item'] = new_rating['item'].astype(str)
			new_rating = new_rating.set_index(["item", "user"])
			df = pd.concat([df, new_rating])
		
		df.to_csv("ratings.csv")
		
		result = {}
		result["status"] = "Ok"
		return result

	result = {}
	result["status"] = "Error"
	return result

def like(request):
	user = request["user"]
	item = request["item"]
	rating = 1

	return commit_rating(user, item, rating)

def dislike(request):
	user = request["user"]
	item = request["item"]
	rating = 0

	return commit_rating(user, item, rating)