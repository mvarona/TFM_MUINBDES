from flask import Flask, render_template, abort
import random_municipality
import sanitize_names
import get_municipality
import make_decimal_numbers
import json

app = Flask(__name__)

app.domain = 'http://127.0.0.1:5000'

@app.route('/')
@app.route("/inicio")
def home():
	return render_template('home.html', domain=app.domain)

@app.route('/random-municipality')
def load_random_municipality():
	try:
		response = json.loads(random_municipality.get_random_municipality("database.json", "wikipedia.json", True))
		province = response["data"]["provincia"].lower()
		municipality = response["data"]["municipio"]
		province = sanitize_names.make_url_name(province)
		municipality = sanitize_names.make_url_name(municipality)
		return app.redirect("/" + province + "/" + municipality, code=302)
	except Exception as e:
		abort(500)

@app.route('/<province>/<municipality>')
def load_municipality(province, municipality):

	return app.send_static_file('municipios/' + province + '/' + municipality + ".html")

	# Uncomment to test the template:
	# try:
	# 	response = get_municipality.get_municipality_info("28079")
	# except Exception as e:
	# 	abort(404)
	# return render_template('municipality.html', domain=app.domain, municipality_info = json.dumps(response), 
	# 	codigo_ine = response["codigo_ine"],
	# 	municipio = response["data"]["municipio"],
	# 	provincia = response["data"]["provincia"],
	# 	comunidad_autonoma = response["data"]["comunidad_autonoma"],
	# 	municipio_nombre_humano = response["data"]["municipio_nombre_humano"],
	# 	num_centros_salud = response["data"]["num_centros_salud"],
	# 	num_centros_urgencias = response["data"]["num_centros_urgencias"],
	# 	num_hospitales = response["data"]["num_hospitales"],
	# 	num_colegios = make_decimal_numbers.convert_decimal_numbers(response["data"]["num_colegios"]),
	# 	num_universidades = response["data"]["num_universidades"],
	# 	linea_costa_provincia = response["data"]["linea_costa_provincia"],
	# 	linea_montana_provincia = response["data"]["linea_montana_provincia"],
	# 	poblacion = make_decimal_numbers.convert_decimal_numbers(response["data"]["poblacion"]),
	# 	superficie = response["data"]["superficie"],
	# 	densidad_poblacion = make_decimal_numbers.convert_decimal_numbers(response["data"]["densidad_poblacion"]),
	# 	lat = response["data"]["lat"],
	# 	lon = response["data"]["lon"],
	# 	feb_avg_min_temp = int(response["data"]["feb_avg_min_temp"]),
	# 	feb_avg_max_temp = int(response["data"]["feb_avg_max_temp"]),
	# 	feb_avg_temp = int(response["data"]["feb_avg_temp"]),
	# 	feb_avg_humidity = response["data"]["feb_avg_humidity"],
	# 	feb_avg_wind = response["data"]["feb_avg_wind"],
	# 	feb_avg_min_rain = response["data"]["feb_avg_min_rain"],
	# 	feb_avg_max_rain = response["data"]["feb_avg_max_rain"],
	# 	feb_avg_rain = make_decimal_numbers.convert_decimal_numbers(response["data"]["feb_avg_rain"], False),
	# 	feb_avg_clouds = response["data"]["feb_avg_clouds"],
	# 	feb_avg_sunshine_hours = response["data"]["feb_avg_sunshine_hours"],
	# 	jul_avg_min_temp = int(response["data"]["jul_avg_min_temp"]),
	# 	jul_avg_max_temp = int(response["data"]["jul_avg_max_temp"]),
	# 	jul_avg_temp = int(response["data"]["jul_avg_temp"]),
	# 	jul_avg_humidity = response["data"]["jul_avg_humidity"],
	# 	jul_avg_wind = response["data"]["jul_avg_wind"],
	# 	jul_avg_min_rain = response["data"]["jul_avg_min_rain"],
	# 	jul_avg_max_rain = response["data"]["jul_avg_max_rain"],
	# 	jul_avg_rain = make_decimal_numbers.convert_decimal_numbers(response["data"]["jul_avg_rain"], False),
	# 	jul_avg_clouds = response["data"]["jul_avg_clouds"],
	# 	jul_avg_sunshine_hours = response["data"]["jul_avg_sunshine_hours"],
	# 	kms_capital_provincia = int(response["data"]["kms_capital_provincia"]),
	# 	altitud = response["data"]["altitud"],
	# 	renta_bruta_media = make_decimal_numbers.convert_decimal_numbers(response["data"]["renta_bruta_media"]),
	# 	precio_m2_venta = make_decimal_numbers.convert_decimal_numbers(response["data"]["precio_m2_venta"]),
	# 	num_casas_venta = make_decimal_numbers.convert_decimal_numbers(response["data"]["num_casas_venta"]),
	# 	precio_m2_alquiler = make_decimal_numbers.convert_decimal_numbers(response["data"]["precio_m2_alquiler"]),
	# 	num_casas_alquiler = make_decimal_numbers.convert_decimal_numbers(response["data"]["num_casas_alquiler"]),
	# 	precio_m2_venta_provincia = make_decimal_numbers.convert_decimal_numbers(response["data"]["precio_m2_venta_provincia"]),
	# 	precio_medio_venta_provincia = make_decimal_numbers.convert_decimal_numbers(response["data"]["precio_medio_venta_provincia"]),
	# 	precio_m2_alquiler_provincia = make_decimal_numbers.convert_decimal_numbers(response["data"]["precio_m2_alquiler_provincia"]),
	# 	precio_medio_alquiler_provincia = make_decimal_numbers.convert_decimal_numbers(response["data"]["precio_medio_alquiler_provincia"]),
	# 	tasa_actividad_provincia = response["data"]["tasa_actividad_provincia"],
	# 	tasa_paro_provincia = make_decimal_numbers.convert_decimal_numbers(response["data"]["tasa_paro_provincia"], False),
	# 	tasa_empleo_provincia = response["data"]["tasa_empleo_provincia"],
	# 	num_empleos_provincia = make_decimal_numbers.convert_decimal_numbers(response["data"]["num_empleos_provincia"]),
	# 	cobertura_30 = int(response["data"]["cobertura_30"]),
	# 	cobertura_100 = int(response["data"]["cobertura_100"]),
	# 	cobertura_3g = int(response["data"]["cobertura_3g"]),
	# 	cobertura_4g = int(response["data"]["cobertura_4g"]),
	# 	sitios_comercio = response["data"]["sitios_comercio"],
	# 	sitios_turismo = response["data"]["sitios_turismo"],
	# 	sitios_alojamiento = response["data"]["sitios_alojamiento"],
	# 	sitios_ocio = response["data"]["sitios_ocio"],
	# 	sitios_natural = response["data"]["sitios_natural"],
	# 	sitios_servicio = response["data"]["sitios_servicio"],
	# 	sitios_actividad = response["data"]["sitios_actividad"],
	# 	sitios_entretenimiento = response["data"]["sitios_entretenimiento"],
	# 	sitios_catering = response["data"]["sitios_catering"],
	# 	sitios_sport = response["data"]["sitios_sport"],
	# 	sitios_edificio	= response["data"]["sitios_edificio"],
	# 	sitios_acceso_limitado = response["data"]["sitios_acceso_limitado"],
	# 	sitios_artificial = response["data"]["sitios_artificial"],
	# 	sitios_acceso = response["data"]["sitios_acceso"],
	# 	sitios_sin_acceso = response["data"]["sitios_sin_acceso"],
	# 	sitios_patrimonio = response["data"]["sitios_patrimonio"],
	# 	sitios_carretera = response["data"]["sitios_carretera"],
	# 	sitios_cuota = response["data"]["sitios_cuota"],
	# 	sitios_comodidad = response["data"]["sitios_comodidad"],
	# 	text = response["data"]["text"],
	# 	url = response["data"]["url"],
	# 	images = response["data"]["images"]
	# )

@app.route('/generate-municipalities-pages')
def generate_municipalities_pages():
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