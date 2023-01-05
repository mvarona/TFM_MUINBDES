#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a CSV with some random ratings

import pandas as pd
import sys
import os
import re

def main(argv):
	if (len(sys.argv) < 3):
		print('Uso: python3 create_ratings.py database.csv users.csv')
		sys.exit(2)
	database_fn = sys.argv[1]
	users_fn = sys.argv[2]
	new_fn = "ratings_dataset" + ".csv"
	df = pd.read_csv(database_fn)
	users = pd.read_csv(users_fn)

	users = users["user_id"].tolist()

	ratings = pd.DataFrame(columns=["item", "user", "rating"])
	ratings = ratings.set_index(["item", "user"])

	i = 0
	for user in users:

		if i == 0:
			# Le gusta la playa, no le gusta la montaña:
			municipalities = df[df["linea_costa_provincia"] == 1]
			municipalities = df[df["altitud"] < 50]["codigo_ine"].sample(100).tolist()
			users = [user for i in range(100)]
			users_ratings = [1 for i in range(100)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			municipalities = df[df["linea_montana_provincia"] == 1]
			municipalities = df[df["altitud"] > 900]["codigo_ine"].sample(100).tolist()
			users = [user for i in range(100)]
			users_ratings = [0 for i in range(100)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			ratings.to_csv(new_fn)

		if i == 1:
			# Le gusta la montaña, no le gusta la playa:
			municipalities = df[df["linea_costa_provincia"] == 1]
			municipalities = df[df["altitud"] < 50]["codigo_ine"].sample(100).tolist()
			users = [user for i in range(100)]
			users_ratings = [0 for i in range(100)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			municipalities = df[df["linea_montana_provincia"] == 1]
			municipalities = df[df["altitud"] > 900]["codigo_ine"].sample(100).tolist()
			users = [user for i in range(100)]
			users_ratings = [1 for i in range(100)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			ratings.to_csv(new_fn)

		if i == 2:
			# Le gustan los pueblos de menos de 1000 habitantes, no le gustan los demás:
			municipalities = df[df["poblacion"] < 1000]["codigo_ine"].sample(100).tolist()
			users = [user for i in range(100)]
			users_ratings = [1 for i in range(100)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			municipalities = df[df["poblacion"] > 1000]["codigo_ine"].sample(100).tolist()
			users = [user for i in range(100)]
			users_ratings = [0 for i in range(100)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			ratings.to_csv(new_fn)

		if i == 3:
			# Le gustan los pueblos de 1000 a 5000 habitantes, no le gustan de más:
			municipalities = df[df["poblacion"] > 1000]
			municipalities = df[df["poblacion"] < 5000]
			municipalities = municipalities["codigo_ine"].sample(100).tolist()
			users = [user for i in range(100)]
			users_ratings = [1 for i in range(100)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			municipalities = df[df["poblacion"] > 5000]
			municipalities = municipalities["codigo_ine"].sample(100).tolist()
			users = [user for i in range(100)]
			users_ratings = [0 for i in range(100)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			ratings.to_csv(new_fn)

		if i == 4:
			# Le gustan los pueblos de 10000 habitantes, no le gustan de más:
			municipalities = df[df["poblacion"] > 5000]
			municipalities = df[df["poblacion"] < 10000]
			municipalities = municipalities["codigo_ine"].sample(100).tolist()
			users = [user for i in range(100)]
			users_ratings = [1 for i in range(100)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			municipalities = df[df["poblacion"] > 10000]
			municipalities = municipalities["codigo_ine"].sample(100).tolist()
			users = [user for i in range(100)]
			users_ratings = [0 for i in range(100)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			ratings.to_csv(new_fn)

		if i == 5:
			# Le gustan las ciudades de 50-70000 habitantes, no le gustan de más:
			municipalities = df[df["poblacion"] > 50000]
			municipalities = df[df["poblacion"] < 70000]
			municipalities = municipalities["codigo_ine"].sample(100).tolist()
			users = [user for i in range(100)]
			users_ratings = [1 for i in range(100)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			municipalities = df[df["poblacion"] > 70000]
			municipalities = municipalities["codigo_ine"].sample(100).tolist()
			users = [user for i in range(100)]
			users_ratings = [0 for i in range(100)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			ratings.to_csv(new_fn)

		if i == 6:
			# Le gustan las ciudades de 100-200000 habitantes, no le gustan de más, ni de menos:
			municipalities = df[df["poblacion"] > 100000]
			municipalities = df[df["poblacion"] < 200000]
			municipalities = municipalities["codigo_ine"].sample(100).tolist()
			users = [user for i in range(100)]
			users_ratings = [1 for i in range(100)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			municipalities = df[df["poblacion"] > 200000]
			municipalities = municipalities["codigo_ine"].sample(25).tolist()
			users = [user for i in range(25)]
			users_ratings = [0 for i in range(25)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			ratings.to_csv(new_fn)

			municipalities = df[df["poblacion"] < 100000]
			municipalities = municipalities["codigo_ine"].sample(75).tolist()
			users = [user for i in range(75)]
			users_ratings = [0 for i in range(75)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			ratings.to_csv(new_fn)

		if i == 7:
			# Le gustan las ciudades de 200-500000 habitantes, no le gustan de más, ni de menos:
			municipalities = df[df["poblacion"] > 200000]
			municipalities = df[df["poblacion"] < 500000]
			municipalities = municipalities["codigo_ine"].sample(100).tolist()
			users = [user for i in range(100)]
			users_ratings = [1 for i in range(100)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			municipalities = df[df["poblacion"] > 500000]
			municipalities = municipalities["codigo_ine"].sample(5).tolist()
			users = [user for i in range(5)]
			users_ratings = [0 for i in range(5)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			ratings.to_csv(new_fn)


			municipalities = df[df["poblacion"] < 200000]
			municipalities = municipalities["codigo_ine"].sample(95).tolist()
			users = [user for i in range(95)]
			users_ratings = [0 for i in range(95)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			ratings.to_csv(new_fn)
		
		if i == 8:
			# Le gustan los pueblos de menos de 10.000 habitantes con fibra óptica, no le gustan los que no tienen:
			municipalities = df[df["poblacion"] < 10000]
			municipalities = df[df["cobertura_100"] > 50]
			municipalities = municipalities["codigo_ine"].sample(100).tolist()
			users = [user for i in range(100)]
			users_ratings = [1 for i in range(100)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			municipalities = df[df["poblacion"] < 10000]
			municipalities = df[df["cobertura_100"] < 50]
			municipalities = municipalities["codigo_ine"].sample(100).tolist()
			users = [user for i in range(100)]
			users_ratings = [0 for i in range(100)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			ratings.to_csv(new_fn)

		if i == 9:
			# Le gustan los pueblos de menos de 10.000 habitantes con centros de salud, no le gustan los que no tienen:
			municipalities = df[df["poblacion"] < 10000]
			municipalities = df[df["num_centros_salud"] > 0]
			municipalities = municipalities["codigo_ine"].sample(100).tolist()
			users = [user for i in range(100)]
			users_ratings = [1 for i in range(100)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			municipalities = df[df["poblacion"] < 10000]
			municipalities = df[df["num_centros_salud"] == 0]
			municipalities = municipalities["codigo_ine"].sample(100).tolist()
			users = [user for i in range(100)]
			users_ratings = [0 for i in range(100)]

			new_ratings = pd.DataFrame({
				"item":municipalities,
				"user":users,
				"rating":users_ratings
			})
			new_ratings = new_ratings.set_index(["item", "user"])
			ratings = pd.concat([ratings, new_ratings])

			ratings.to_csv(new_fn)

		i += 1


if __name__ == "__main__":
	main(sys.argv)
