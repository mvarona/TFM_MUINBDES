import pandas as pd
from surprise import Dataset
from surprise import Reader
from surprise import KNNWithMeans
from sklearn.model_selection import train_test_split
from surprise.model_selection import cross_validate
from surprise import BaselineOnly
from surprise import accuracy

from sklearn.utils import shuffle

def create_users_recommendations():
	df = pd.read_csv("ratings.csv")
	df = shuffle(df)
	reader = Reader(rating_scale=(0, 1))
	
	# sim_options = {
	#     "name": "cosine"
	# }
	# algo = KNNWithMeans(sim_options=sim_options)

	bsl_options = {
		'method': 'als',
		'n_epochs': 3
	}
	algo = BaselineOnly(bsl_options=bsl_options)
	
	trainset, testset = train_test_split(df, test_size=.3)
	train_dataset = Dataset.load_from_df(trainset[["item", "user", "rating"]], reader)
	train_dataset = train_dataset.build_full_trainset()

	test_dataset = Dataset.load_from_df(testset[["item", "user", "rating"]], reader)
	test_dataset = train_dataset.build_anti_testset()
	
	algo.fit(train_dataset)

	# predictions = algo.test(test_dataset)
	# accuracy.rmse(predictions)

	municipalities = df["item"].unique().tolist()
	users = df["user"].unique().tolist()

	predictions = {}

	print(algo.predict("l8iD-yrO-QvVdeKcGGHAyhlUwHaJIbjF", "48044").est)
	print(algo.predict("LLM6-Kuq-TpiQBUBqBCmCstl2TtkIQFP", "07046").est)
	print(algo.predict("LLM7-Kuq-TpiQBUBqBCmCstl2TtkIQFP", "03099").est)

	# for user in users:

	# 	print("USUARIO: ")
	# 	print(user)

	# 	user_predictions = {}

	# 	for municipality in municipalities:
	# 		prediction = algo.predict(user, municipality).est
	# 		if prediction > 0.5:
	# 			if municipality not in user_predictions:
	# 				user_predictions[municipality] = 0
	# 			user_predictions[municipality] = prediction


		# user_predictions_sorted = dict(sorted(user_predictions.items(), key=lambda item: item[1]))
		# print(len(user_predictions_sorted))
		# print(user_predictions_sorted)

	#	break
		





create_users_recommendations()