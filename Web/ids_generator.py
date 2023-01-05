import pandas as pd
import random
import string
import time
import datetime

def create_user_id():
	users = pd.read_csv("users.csv")
	ids = users["user_id"].tolist()
	
	chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
	user_id_length = 30
	new_id = ''.join(random.choice(chars) for x in range(user_id_length))
	new_id = new_id[:4] + "-" + new_id[4:]
	new_id = new_id[:8] + "-" + new_id[8:]

	while (new_id in ids):
		new_id = ''.join(random.choice(chars) for x in range(user_id_length))
		new_id = new_id[:4] + "-" + new_id[4:]
		new_id = new_id[:8] + "-" + new_id[8:]

	dts = datetime.datetime.utcnow()
	unixtimestamp = round(time.mktime(dts.timetuple()) + dts.microsecond/1e6)

	new_user = pd.DataFrame({
		"user_id":[new_id],
		"creation_timestamp":[unixtimestamp]
	})
	users = pd.concat([users, new_user])

	users.to_csv("users.csv", index=False)

	return new_id