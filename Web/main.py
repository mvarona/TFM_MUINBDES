from flask import Flask, render_template, abort, request, redirect
import random_municipality
import random_background
import sanitize_names
import get_municipality
import make_decimal_numbers
import recommender
import survey
import ratings_manager
import json
import os
import requests

app = Flask(__name__)

app.domain = 'http://localhost:5000'
app.mode = "Debug"

#app.domain = 'https://www.dondeteesperan.es'
#app.mode = "Production"

@app.route('/')
@app.route("/inicio")
def home():
	fallback_background = random_background.get_random_background()
	return render_template(
		'home.html',
		domain=app.domain,
		images = [],
		fallback_background_name = fallback_background[0],
		fallback_background_img = fallback_background[1],
		fallback_background_user = fallback_background[2],
		fallback_background_attr = fallback_background[3]
	)

@app.route('/municipio-aleatorio')
def load_random_municipality():
	try:
		response = json.loads(random_municipality.get_random_municipality("database.json", "wikipedia.json", True))
		province = response["data"]["provincia"]
		municipality = response["data"]["municipio"]
		province = sanitize_names.make_url_name(province)
		municipality = sanitize_names.make_url_name(municipality)
		return redirect(app.domain + '/' + province + '/' + municipality, code=302)
	except:
		abort(500)

@app.route('/municipio-parecido')
def load_similar_municipality():
	fallback_background = random_background.get_random_background()
	return render_template(
		'similar.html',
		domain=app.domain,
		images = [],
		fallback_background_name = fallback_background[0],
		fallback_background_img = fallback_background[1],
		fallback_background_user = fallback_background[2],
		fallback_background_attr = fallback_background[3],
		section = "municipio_parecido"
	)

@app.route('/<province>/<municipality>')
def load_municipality(province, municipality):
	return app.send_static_file('municipios/' + province + '/' + municipality + ".html")

@app.route('/recomendar/<nsi_code>')
def recommend(nsi_code):
	try:
		recommender_response = json.loads(recommender.recommend(nsi_code))
		recommended_nsi_code = list(recommender_response["data"].keys())[1]
		response = get_municipality.get_municipality_info(recommended_nsi_code)
		province = response["data"]["provincia"]
		province_human_name = response["data"]["provincia"]
		municipality = response["data"]["municipio"]
		municipality_human_name = response["data"]["municipio_nombre_humano"]
		province = sanitize_names.make_url_name(province)
		municipality = sanitize_names.make_url_name(municipality)
		result = {}
		result["status"] = "Ok"
		result["data"] = {}
		result["data"]["codigo_ine"] = recommended_nsi_code
		result["data"]["provincia_path"] = province
		result["data"]["municipio_path"] = municipality
		result["data"]["municipio_nombre_humano"] = municipality_human_name
		result["data"]["provincia_nombre_humano"] = province_human_name
		result["data"]["url"] = "/" + province + "/" + municipality
		return result
	except:
		abort(500)

@app.route('/municipio-personalizado')
def custom_municipality():
	fallback_background = random_background.get_random_background()
	return render_template(
		'survey.html',
		domain = app.domain,
		images = [],
		fallback_background_name = fallback_background[0],
		fallback_background_img = fallback_background[1],
		fallback_background_user = fallback_background[2],
		fallback_background_attr = fallback_background[3],
		section = "municipio_personalizado"
	)

@app.route('/cuestionario', methods=['POST'])
def municipality_survey():
	try:
		response = survey.get_survey_recommendation(request.form)
		recommended_nsi_code = response["codigo_ine"]
		result = {}

		if recommended_nsi_code == "00000":
			result["status"] = "Ok"
			result["data"] = {}
			result["data"]["codigo_ine"] = recommended_nsi_code
			result["data"]["provincia_path"] = ""
			result["data"]["municipio_path"] = ""
			result["data"]["url"] = ""

		else:
			province = response["provincia"]
			municipality = response["municipio"]
			province = sanitize_names.make_url_name(province)
			municipality = sanitize_names.make_url_name(municipality)
			result["status"] = "Ok"
			result["data"] = {}
			result["data"]["codigo_ine"] = recommended_nsi_code
			result["data"]["provincia_path"] = province
			result["data"]["municipio_path"] = municipality
			result["data"]["url"] = "/" + province + "/" + municipality

		return result
	except:
		abort(500)

@app.route('/generate-user-id')
def create_user_id():
	try:
		url = "https://www.bmsalamanca.com/others/dondeteesperan/api/generate-user-id"
		params = {"auth_token": "8DUJdMxsRxlTCa5w6egi6mY9g6NWORTUDBuS1uig"}
		new_id = requests.post(url, data=params)
		return new_id.text
	except:
		abort(500)

@app.route('/like', methods=['POST'])
def like():
	try:
		url = "https://www.bmsalamanca.com/others/dondeteesperan/api/rate"
		params = {
			"auth_token": "8DUJdMxsRxlTCa5w6egi6mY9g6NWORTUDBuS1uig",
			"item": request.form["item"],
			"user": request.form["user"],
			"rating": 1
		}
		response = requests.post(url, data=params)
		return response.text
	except:
		abort(500)

@app.route('/dislike', methods=['POST'])
def dislike():
	try:
		url = "https://www.bmsalamanca.com/others/dondeteesperan/api/rate"
		params = {
			"auth_token": "8DUJdMxsRxlTCa5w6egi6mY9g6NWORTUDBuS1uig",
			"item": request.form["item"],
			"user": request.form["user"],
			"rating": 0
		}
		response = requests.post(url, data=params)
		return response.text
	except:
		abort(500)

@app.route('/metodologia')
def methodology():
	try:
		fallback_background = random_background.get_random_background()
		return render_template(
			'metodologia.html',
			domain = app.domain,
			images = [],
			fallback_background_name = fallback_background[0],
			fallback_background_img = fallback_background[1],
			fallback_background_user = fallback_background[2],
			fallback_background_attr = fallback_background[3]
		)
	except:
		abort(500)

@app.route('/generate-municipalities-pages')
def generate_municipalities_pages():
	if app.mode != "Debug":
		abort(404)
	else:
		with open("database.json", 'r') as f:
			database = json.load(f)

		for code in database:

			response = get_municipality.get_municipality_info(code)
			
			out = render_template('municipality.html', domain=app.domain, municipality_info = json.dumps(response), 
				codigo_ine = response["codigo_ine"],
				municipio = response["data"]["municipio"],
				provincia = response["data"]["provincia"],
				comunidad_autonoma = response["data"]["comunidad_autonoma"],
				municipio_nombre_humano = response["data"]["municipio_nombre_humano"],
				num_centros_salud = response["data"]["num_centros_salud"],
				num_centros_urgencias = response["data"]["num_centros_urgencias"],
				num_hospitales = response["data"]["num_hospitales"],
				num_colegios = make_decimal_numbers.convert_decimal_numbers(response["data"]["num_colegios"]),
				num_universidades = response["data"]["num_universidades"],
				linea_costa_provincia = response["data"]["linea_costa_provincia"],
				linea_montana_provincia = response["data"]["linea_montana_provincia"],
				poblacion = make_decimal_numbers.convert_decimal_numbers(response["data"]["poblacion"]),
				superficie = response["data"]["superficie"],
				densidad_poblacion = make_decimal_numbers.convert_decimal_numbers(response["data"]["densidad_poblacion"]),
				lat = response["data"]["lat"],
				lon = response["data"]["lon"],
				feb_avg_min_temp = int(response["data"]["feb_avg_min_temp"]),
				feb_avg_max_temp = int(response["data"]["feb_avg_max_temp"]),
				feb_avg_temp = int(response["data"]["feb_avg_temp"]),
				feb_avg_humidity = response["data"]["feb_avg_humidity"],
				feb_avg_wind = response["data"]["feb_avg_wind"],
				feb_avg_min_rain = response["data"]["feb_avg_min_rain"],
				feb_avg_max_rain = response["data"]["feb_avg_max_rain"],
				feb_avg_rain = make_decimal_numbers.convert_decimal_numbers(response["data"]["feb_avg_rain"], False),
				feb_avg_clouds = response["data"]["feb_avg_clouds"],
				feb_avg_sunshine_hours = response["data"]["feb_avg_sunshine_hours"],
				jul_avg_min_temp = int(response["data"]["jul_avg_min_temp"]),
				jul_avg_max_temp = int(response["data"]["jul_avg_max_temp"]),
				jul_avg_temp = int(response["data"]["jul_avg_temp"]),
				jul_avg_humidity = response["data"]["jul_avg_humidity"],
				jul_avg_wind = response["data"]["jul_avg_wind"],
				jul_avg_min_rain = response["data"]["jul_avg_min_rain"],
				jul_avg_max_rain = response["data"]["jul_avg_max_rain"],
				jul_avg_rain = make_decimal_numbers.convert_decimal_numbers(response["data"]["jul_avg_rain"], False),
				jul_avg_clouds = response["data"]["jul_avg_clouds"],
				jul_avg_sunshine_hours = response["data"]["jul_avg_sunshine_hours"],
				kms_capital_provincia = int(response["data"]["kms_capital_provincia"]),
				altitud = response["data"]["altitud"],
				renta_bruta_media = make_decimal_numbers.convert_decimal_numbers(response["data"]["renta_bruta_media"]),
				precio_m2_venta = make_decimal_numbers.convert_decimal_numbers(response["data"]["precio_m2_venta"]),
				num_casas_venta = make_decimal_numbers.convert_decimal_numbers(response["data"]["num_casas_venta"]),
				precio_m2_alquiler = make_decimal_numbers.convert_decimal_numbers(response["data"]["precio_m2_alquiler"]),
				num_casas_alquiler = make_decimal_numbers.convert_decimal_numbers(response["data"]["num_casas_alquiler"]),
				precio_m2_venta_provincia = make_decimal_numbers.convert_decimal_numbers(response["data"]["precio_m2_venta_provincia"]),
				precio_medio_venta_provincia = make_decimal_numbers.convert_decimal_numbers(response["data"]["precio_medio_venta_provincia"]),
				precio_m2_alquiler_provincia = make_decimal_numbers.convert_decimal_numbers(response["data"]["precio_m2_alquiler_provincia"]),
				precio_medio_alquiler_provincia = make_decimal_numbers.convert_decimal_numbers(response["data"]["precio_medio_alquiler_provincia"]),
				tasa_actividad_provincia = response["data"]["tasa_actividad_provincia"],
				tasa_paro_provincia = make_decimal_numbers.convert_decimal_numbers(response["data"]["tasa_paro_provincia"], False),
				tasa_empleo_provincia = response["data"]["tasa_empleo_provincia"],
				num_empleos_provincia = make_decimal_numbers.convert_decimal_numbers(response["data"]["num_empleos_provincia"]),
				cobertura_30 = int(response["data"]["cobertura_30"]),
				cobertura_100 = int(response["data"]["cobertura_100"]),
				cobertura_3g = int(response["data"]["cobertura_3g"]),
				cobertura_4g = int(response["data"]["cobertura_4g"]),
				sitios_comercio = response["data"]["sitios_comercio"],
				sitios_turismo = response["data"]["sitios_turismo"],
				sitios_alojamiento = response["data"]["sitios_alojamiento"],
				sitios_ocio = response["data"]["sitios_ocio"],
				sitios_natural = response["data"]["sitios_natural"],
				sitios_servicio = response["data"]["sitios_servicio"],
				sitios_actividad = response["data"]["sitios_actividad"],
				sitios_entretenimiento = response["data"]["sitios_entretenimiento"],
				sitios_catering = response["data"]["sitios_catering"],
				sitios_sport = response["data"]["sitios_sport"],
				sitios_edificio = response["data"]["sitios_edificio"],
				sitios_acceso_limitado = response["data"]["sitios_acceso_limitado"],
				sitios_artificial = response["data"]["sitios_artificial"],
				sitios_acceso = response["data"]["sitios_acceso"],
				sitios_sin_acceso = response["data"]["sitios_sin_acceso"],
				sitios_patrimonio = response["data"]["sitios_patrimonio"],
				sitios_carretera = response["data"]["sitios_carretera"],
				sitios_cuota = response["data"]["sitios_cuota"],
				sitios_comodidad = response["data"]["sitios_comodidad"],
				text = response["data"]["text"],
				url = response["data"]["url"],
				images = response["data"]["images"]
			)
			
			province = sanitize_names.make_url_name(response["data"]["provincia"])
			municipality = sanitize_names.make_url_name(response["data"]["municipio_nombre_humano"])
			print("Guardando " + province + "/" + municipality + ".html")
			with open("static/municipios/" + province + "/" + municipality + ".html", "w+") as f:
				f.write(out)

		return "OK!"


@app.route('/test-municipality-page')
def test_municipality():

	if app.mode != "Debug":
		abort(404)
	else:
		# Uncomment to test the template:
		try:
			response = get_municipality.get_municipality_info("37362")
			fallback_background = random_background.get_random_background()
		except Exception as e:
			abort(404)
		return render_template('municipality.html', domain=app.domain, municipality_info = json.dumps(response), 
			codigo_ine = response["codigo_ine"],
			municipio = response["data"]["municipio"],
			provincia = response["data"]["provincia"],
			comunidad_autonoma = response["data"]["comunidad_autonoma"],
			municipio_nombre_humano = response["data"]["municipio_nombre_humano"],
			num_centros_salud = response["data"]["num_centros_salud"],
			num_centros_urgencias = response["data"]["num_centros_urgencias"],
			num_hospitales = response["data"]["num_hospitales"],
			num_colegios = make_decimal_numbers.convert_decimal_numbers(response["data"]["num_colegios"]),
			num_universidades = response["data"]["num_universidades"],
			linea_costa_provincia = response["data"]["linea_costa_provincia"],
			linea_montana_provincia = response["data"]["linea_montana_provincia"],
			poblacion = make_decimal_numbers.convert_decimal_numbers(response["data"]["poblacion"]),
			superficie = response["data"]["superficie"],
			densidad_poblacion = make_decimal_numbers.convert_decimal_numbers(response["data"]["densidad_poblacion"]),
			lat = response["data"]["lat"],
			lon = response["data"]["lon"],
			feb_avg_min_temp = int(response["data"]["feb_avg_min_temp"]),
			feb_avg_max_temp = int(response["data"]["feb_avg_max_temp"]),
			feb_avg_temp = int(response["data"]["feb_avg_temp"]),
			feb_avg_humidity = response["data"]["feb_avg_humidity"],
			feb_avg_wind = response["data"]["feb_avg_wind"],
			feb_avg_min_rain = response["data"]["feb_avg_min_rain"],
			feb_avg_max_rain = response["data"]["feb_avg_max_rain"],
			feb_avg_rain = make_decimal_numbers.convert_decimal_numbers(response["data"]["feb_avg_rain"], False),
			feb_avg_clouds = response["data"]["feb_avg_clouds"],
			feb_avg_sunshine_hours = int(response["data"]["feb_avg_sunshine_hours"]),
			jul_avg_min_temp = int(response["data"]["jul_avg_min_temp"]),
			jul_avg_max_temp = int(response["data"]["jul_avg_max_temp"]),
			jul_avg_temp = int(response["data"]["jul_avg_temp"]),
			jul_avg_humidity = response["data"]["jul_avg_humidity"],
			jul_avg_wind = response["data"]["jul_avg_wind"],
			jul_avg_min_rain = response["data"]["jul_avg_min_rain"],
			jul_avg_max_rain = response["data"]["jul_avg_max_rain"],
			jul_avg_rain = make_decimal_numbers.convert_decimal_numbers(response["data"]["jul_avg_rain"], False),
			jul_avg_clouds = response["data"]["jul_avg_clouds"],
			jul_avg_sunshine_hours = int(response["data"]["jul_avg_sunshine_hours"]),
			kms_capital_provincia = int(response["data"]["kms_capital_provincia"]),
			altitud = response["data"]["altitud"],
			renta_bruta_media = make_decimal_numbers.convert_decimal_numbers(response["data"]["renta_bruta_media"]),
			precio_m2_venta = make_decimal_numbers.convert_decimal_numbers(response["data"]["precio_m2_venta"]),
			num_casas_venta = make_decimal_numbers.convert_decimal_numbers(response["data"]["num_casas_venta"]),
			precio_m2_alquiler = make_decimal_numbers.convert_decimal_numbers(response["data"]["precio_m2_alquiler"]),
			num_casas_alquiler = make_decimal_numbers.convert_decimal_numbers(response["data"]["num_casas_alquiler"]),
			precio_m2_venta_provincia = make_decimal_numbers.convert_decimal_numbers(response["data"]["precio_m2_venta_provincia"]),
			precio_medio_venta_provincia = make_decimal_numbers.convert_decimal_numbers(response["data"]["precio_medio_venta_provincia"]),
			precio_m2_alquiler_provincia = make_decimal_numbers.convert_decimal_numbers(response["data"]["precio_m2_alquiler_provincia"]),
			precio_medio_alquiler_provincia = make_decimal_numbers.convert_decimal_numbers(response["data"]["precio_medio_alquiler_provincia"]),
			tasa_actividad_provincia = response["data"]["tasa_actividad_provincia"],
			tasa_paro_provincia = make_decimal_numbers.convert_decimal_numbers(response["data"]["tasa_paro_provincia"], False),
			tasa_empleo_provincia = response["data"]["tasa_empleo_provincia"],
			num_empleos_provincia = make_decimal_numbers.convert_decimal_numbers(response["data"]["num_empleos_provincia"]),
			cobertura_30 = int(response["data"]["cobertura_30"]),
			cobertura_100 = int(response["data"]["cobertura_100"]),
			cobertura_3g = int(response["data"]["cobertura_3g"]),
			cobertura_4g = int(response["data"]["cobertura_4g"]),
			sitios_comercio = response["data"]["sitios_comercio"],
			sitios_turismo = response["data"]["sitios_turismo"],
			sitios_alojamiento = response["data"]["sitios_alojamiento"],
			sitios_ocio = response["data"]["sitios_ocio"],
			sitios_natural = response["data"]["sitios_natural"],
			sitios_servicio = response["data"]["sitios_servicio"],
			sitios_actividad = response["data"]["sitios_actividad"],
			sitios_entretenimiento = response["data"]["sitios_entretenimiento"],
			sitios_catering = response["data"]["sitios_catering"],
			sitios_sport = response["data"]["sitios_sport"],
			sitios_edificio	= response["data"]["sitios_edificio"],
			sitios_acceso_limitado = response["data"]["sitios_acceso_limitado"],
			sitios_artificial = response["data"]["sitios_artificial"],
			sitios_acceso = response["data"]["sitios_acceso"],
			sitios_sin_acceso = response["data"]["sitios_sin_acceso"],
			sitios_patrimonio = response["data"]["sitios_patrimonio"],
			sitios_carretera = response["data"]["sitios_carretera"],
			sitios_cuota = response["data"]["sitios_cuota"],
			sitios_comodidad = response["data"]["sitios_comodidad"],
			text = response["data"]["text"],
			url = response["data"]["url"],
			images = response["data"]["images"],
			fallback_background_name = fallback_background[0],
			fallback_background_img = fallback_background[1],
			fallback_background_user = fallback_background[2],
			fallback_background_attr = fallback_background[3]
		)

@app.errorhandler(404)
def page_not_found(e):
	fallback_background = random_background.get_random_background()
	return render_template('404.html',
		fallback_background_name = fallback_background[0],
		fallback_background_img = fallback_background[1],
		fallback_background_user = fallback_background[2],
		fallback_background_attr = fallback_background[3]), 404

if __name__ == "__main__":
	if app.mode == "Debug":
		app.run(debug=True)
	else:
		app.run(debug=False)