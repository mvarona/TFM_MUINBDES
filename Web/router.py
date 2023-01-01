from flask import Flask, render_template, abort
import random_municipality
import sanitize_names
import json

app = Flask(__name__)

app.domain = 'http://127.0.0.1:5000'

@app.route('/')
def home():
	return render_template('home.html', domain=app.domain)

@app.route('/random-municipality')
def return_random_municipality():
	try:
		response = json.loads(random_municipality.get_random_municipality("database.json", "wikipedia.json", True))
		province = response["data"]["provincia"].lower()
		municipality = response["data"]["municipio"]
		province = sanitize_names.make_url_name(province)
		municipality = sanitize_names.make_url_name(municipality)
		return app.redirect("/" + province + "/" + municipality, code=302)
	except Exception as e:
		abort(500)