import pandas as pd

def filter_region(model, comunidad):
	comunidad = int(comunidad)

	if comunidad == 1:
		model = model[model['comunidad_autonoma'] == "Andalucía"]

	elif comunidad == 2:
		model = model[model['comunidad_autonoma'] == "Aragón"]

	elif comunidad == 3:
		model = model[model['comunidad_autonoma'] == "Cantabria"]

	elif comunidad == 4:
		model = model[model['comunidad_autonoma'] == "Castilla y León"]

	elif comunidad == 5:
		model = model[model['comunidad_autonoma'] == "Castilla-La Mancha"]

	elif comunidad == 6:
		model = model[model['comunidad_autonoma'] == "Cataluña"]

	elif comunidad == 7:
		model = model[model['comunidad_autonoma'] == "Ceuta"]

	elif comunidad == 8:
		model = model[model['comunidad_autonoma'] == "Comunidad de Madrid"]

	elif comunidad == 9:
		model = model[model['comunidad_autonoma'] == "Comunidad Foral de Navarra"]

	elif comunidad == 10:
		model = model[model['comunidad_autonoma'] == "Comunidad Valenciana"]

	elif comunidad == 11:
		model = model[model['comunidad_autonoma'] == "Extremadura"]

	elif comunidad == 12:
		model = model[model['comunidad_autonoma'] == "Galicia"]

	elif comunidad == 13:
		model = model[model['comunidad_autonoma'] == "Islas Baleares"]

	elif comunidad == 14:
		model = model[model['comunidad_autonoma'] == "Islas Canarias"]

	elif comunidad == 15:
		model = model[model['comunidad_autonoma'] == "La Rioja"]

	elif comunidad == 16:
		model = model[model['comunidad_autonoma'] == "Melilla"]

	elif comunidad == 17:
		model = model[model['comunidad_autonoma'] == "País Vasco"]

	elif comunidad == 18:
		model = model[model['comunidad_autonoma'] == "Principado de Asturias"]

	elif comunidad == 19:
		model = model[model['comunidad_autonoma'] == "Región de Murcia"]

	else:
		model = model
	
	return model


def filter_province(model, provincia):
	provincia = int(provincia)

	if provincia == 1:
		model = model[model['provincia'] == "A Coruña"]

	if provincia == 2:
		model = model[model['provincia'] == "Álava"]

	if provincia == 3:
		model = model[model['provincia'] == "Albacete"]

	if provincia == 4:
		model = model[model['provincia'] == "Alicante"]

	if provincia == 5:
		model = model[model['provincia'] == "Almería"]

	if provincia == 6:
		model = model[model['provincia'] == "Asturias"]

	if provincia == 7:
		model = model[model['provincia'] == "Ávila"]

	if provincia == 8:
		model = model[model['provincia'] == "Badajoz"]

	if provincia == 9:
		model = model[model['provincia'] == "Barcelona"]

	if provincia == 10:		
		model = model[model['provincia'] == "Bizkaia"]

	if provincia == 11:		
		model = model[model['provincia'] == "Burgos"]

	if provincia == 12:		
		model = model[model['provincia'] == "Cáceres"]

	if provincia == 13:		
		model = model[model['provincia'] == "Cádiz"]

	if provincia == 14:		
		model = model[model['provincia'] == "Cantabria"]

	if provincia == 15:		
		model = model[model['provincia'] == "Castellón"]

	if provincia == 16:		
		model = model[model['provincia'] == "Ceuta"]

	if provincia == 17:		
		model = model[model['provincia'] == "Ciudad Real"]

	if provincia == 18:		
		model = model[model['provincia'] == "Córdoba"]

	if provincia == 19:		
		model = model[model['provincia'] == "Cuenca"]

	if provincia == 20:		
		model = model[model['provincia'] == "Gipuzkoa"]

	if provincia == 21:		
		model = model[model['provincia'] == "Girona"]

	if provincia == 22:		
		model = model[model['provincia'] == "Granada"]

	if provincia == 23:		
		model = model[model['provincia'] == "Guadalajara"]

	if provincia == 24:		
		model = model[model['provincia'] == "Huelva"]

	if provincia == 25:		
		model = model[model['provincia'] == "Huesca"]

	if provincia == 26:		
		model = model[model['provincia'] == "Illes Balears"]

	if provincia == 27:		
		model = model[model['provincia'] == "Jaén"]

	if provincia == 28:		
		model = model[model['provincia'] == "La Rioja"]

	if provincia == 29:		
		model = model[model['provincia'] == "Las Palmas"]

	if provincia == 30:		
		model = model[model['provincia'] == "León"]

	if provincia == 31:		
		model = model[model['provincia'] == "Lleida"]

	if provincia == 32:		
		model = model[model['provincia'] == "Lugo"]

	if provincia == 33:		
		model = model[model['provincia'] == "Madrid"]

	if provincia == 34:		
		model = model[model['provincia'] == "Málaga"]

	if provincia == 35:		
		model = model[model['provincia'] == "Melilla"]

	if provincia == 36:		
		model = model[model['provincia'] == "Murcia"]

	if provincia == 37:		
		model = model[model['provincia'] == "Navarra"]

	if provincia == 38:		
		model = model[model['provincia'] == "Ourense"]

	if provincia == 39:		
		model = model[model['provincia'] == "Palencia"]

	if provincia == 40:		
		model = model[model['provincia'] == "Pontevedra"]

	if provincia == 41:		
		model = model[model['provincia'] == "Salamanca"]

	if provincia == 42:		
		model = model[model['provincia'] == "Santa Cruz de Tenerife"]

	if provincia == 43:		
		model = model[model['provincia'] == "Segovia"]

	if provincia == 44:		
		model = model[model['provincia'] == "Sevilla"]

	if provincia == 45:		
		model = model[model['provincia'] == "Soria"]

	if provincia == 46:		
		model = model[model['provincia'] == "Tarragona"]

	if provincia == 47:		
		model = model[model['provincia'] == "Teruel"]

	if provincia == 48:		
		model = model[model['provincia'] == "Toledo"]

	if provincia == 49:		
		model = model[model['provincia'] == "Valencia"]

	if provincia == 50:		
		model = model[model['provincia'] == "Valladolid"]

	if provincia == 51:		
		model = model[model['provincia'] == "Zamora"]

	if provincia == 52:		
		model = model[model['provincia'] == "Zaragoza"]
	
	else:
		model = model

	return model

def filter_beach(model, playa):
	playa = int(playa)

	if playa == -2:
		model = model[model['linea_costa_provincia'] == 1]

	elif playa == -1:
		model = model[model['linea_costa_provincia'] == 2]

	elif playa == 1:
		model = model[model['linea_costa_provincia'] == 3]

	elif playa == 2:
		model = model[model['linea_costa_provincia'] == 0]

	else:
		model = model

	return model

def filter_mountain(model, montana):
	montana = int(montana)

	if montana == -2:
		model = model[model['linea_montana_provincia'] == 1]

	elif montana == -1:
		model = model[model['linea_montana_provincia'] == 2]

	elif montana == 1:
		model = model[model['linea_montana_provincia'] == 3]

	elif montana == 2:
		model = model[model['linea_montana_provincia'] == 0]

	else:
		model = model

	return model

def filter_health(model, salud):
	salud = int(salud)

	if salud == 1:
		model = model[model['num_centros_salud'] > 0]

	elif salud == 2:
		model = model[model['num_centros_salud'] > 0]
		model = model[model['num_centros_urgencias'] > 0]

	elif salud == 3:
		model = model[model['num_hospitales'] > 0]

	elif salud == 4:
		model = model[model['num_hospitales'] > 0]
		model = model[model['num_centros_urgencias'] > 0]

	else:
		model = model

	return model

def filter_education(model, educacion):
	educacion = int(educacion)

	if educacion == 1:
		model = model[model['num_colegios'] > 0]

	elif educacion == 2:
		model = model[model['num_universidades'] > 0]

	elif educacion == 3:
		model = model[model['num_colegios'] > 0]
		model = model[model['num_universidades'] > 0]

	else:
		model = model

	return model

def filter_population(model, poblacion):
	poblacion = int(poblacion)

	if poblacion == -3:
		model = model[model['poblacion'] <= 1000]

	elif poblacion == -2:
		model = model[model['poblacion'] >= 1000]
		model = model[model['poblacion'] <= 5000]

	elif poblacion == -1:
		model = model[model['poblacion'] >= 5000]
		model = model[model['poblacion'] <= 10000]

	elif poblacion == 1:
		model = model[model['poblacion'] >= 10000]
		model = model[model['poblacion'] <= 100000]

	elif poblacion == 2:
		model = model[model['poblacion'] >= 100000]
		model = model[model['poblacion'] <= 250000]

	elif poblacion == 3:
		model = model[model['poblacion'] >= 250000]

	else:
		model = model

	return model

def filter_twinter(model, tinvierno):
	tinvierno = int(tinvierno)

	if tinvierno == -2:
		model = model[model['feb_avg_temp'] <= 5]

	elif tinvierno == -1:
		model = model[model['feb_avg_temp'] >= 5]
		model = model[model['feb_avg_temp'] <= 10]

	elif tinvierno == 1:
		model = model[model['feb_avg_temp'] >= 10]
		model = model[model['feb_avg_temp'] <= 15]

	elif tinvierno == 2:
		model = model[model['feb_avg_temp'] >= 15]

	else:
		model = model

	return model

def filter_tsummer(model, tverano):
	tverano = int(tverano)

	if tverano == -2:
		model = model[model['jul_avg_temp'] <= 20]

	elif tverano == -1:
		model = model[model['jul_avg_temp'] >= 20]
		model = model[model['jul_avg_temp'] <= 22]

	elif tverano == 1:
		model = model[model['jul_avg_temp'] >= 22]
		model = model[model['jul_avg_temp'] <= 25]

	elif tverano == 2:
		model = model[model['jul_avg_temp'] >= 25]

	else:
		model = model

	return model

def filter_elevation(model, altitud):
	altitud = int(altitud)

	if altitud == -2:
		model = model[model['altitud'] <= 250]

	elif altitud == -1:
		model = model[model['altitud'] >= 250]
		model = model[model['altitud'] <= 500]

	elif altitud == 1:
		model = model[model['altitud'] >= 500]
		model = model[model['altitud'] <= 750]

	elif altitud == 2:
		model = model[model['altitud'] >= 750]

	else:
		model = model

	return model

def filter_distance(model, distancia):
	distancia = int(distancia)

	if distancia == -3:
		model = model[model['kms_capital_provincia'] <= 5]

	elif distancia == -2:
		model = model[model['kms_capital_provincia'] >= 5]
		model = model[model['kms_capital_provincia'] <= 15]

	elif distancia == -1:
		model = model[model['kms_capital_provincia'] >= 15]
		model = model[model['kms_capital_provincia'] <= 25]

	elif distancia == 1:
		model = model[model['kms_capital_provincia'] >= 25]
		model = model[model['kms_capital_provincia'] <= 35]

	elif distancia == 2:
		model = model[model['kms_capital_provincia'] >= 35]
		model = model[model['kms_capital_provincia'] <= 50]

	elif distancia == 3:
		model = model[model['kms_capital_provincia'] >= 50]

	else:
		model = model

	return model

def filter_incomes(model, renta):
	renta = int(renta)

	if renta == -2:
		model = model[model['renta_bruta_media'] <= 20000]

	elif renta == -1:
		model = model[model['renta_bruta_media'] >= 20000]
		model = model[model['renta_bruta_media'] <= 25000]

	elif renta == 1:
		model = model[model['renta_bruta_media'] >= 25000]
		model = model[model['renta_bruta_media'] <= 30000]

	elif renta == 2:
		model = model[model['renta_bruta_media'] >= 30000]

	else:
		model = model

	return model

def filter_connectivity(model, cobertura):
	cobertura = int(cobertura)

	if cobertura == 1:
		model = model[model['cobertura_3g'] >= 50]

	elif cobertura == 2:
		model = model[model['cobertura_4g'] >= 50]

	elif cobertura == 3:
		model = model[model['cobertura_30'] >= 50]

	elif cobertura == 4:
		model = model[model['cobertura_100'] >= 50]

	elif cobertura == 5:
		model = model[model['cobertura_100'] >= 50]
		model = model[model['cobertura_4g'] >= 50]

	else:
		model = model

	return model

def filter_nature(model, naturaleza):
	naturaleza = int(naturaleza)

	if naturaleza == -1:
		a = model[model['sitios_actividad'] != 0]
		b = model[model['sitios_ocio'] != 0]
		c = model[model['sitios_natural'] != 0]
		model = pd.concat([a, b, c]).drop_duplicates().reset_index(drop=True)

	elif naturaleza == 1:
		a = model[model['sitios_comercio'] != 0]
		b = model[model['sitios_servicio'] != 0]
		c = model[model['sitios_catering'] != 0]
		model = pd.concat([a, b, c]).drop_duplicates().reset_index(drop=True)

	else:
		model = model

	return model

def get_survey_recommendation(preferences):
	comunidad = int(preferences["comunidad"])
	provincia = int(preferences["provincia"])
	playa = int(preferences["playa"])
	montana = int(preferences["montana"])
	salud = int(preferences["salud"])
	educacion = int(preferences["educacion"])
	poblacion = int(preferences["poblacion"])
	tinvierno = int(preferences["tinvierno"])
	tverano = int(preferences["tverano"])
	altitud = int(preferences["altitud"])
	distancia = int(preferences["distancia"])
	renta = int(preferences["renta"])
	cobertura = int(preferences["cobertura"])
	naturaleza = int(preferences["naturaleza"])

	model = pd.read_csv("database.csv")
	
	if provincia == 0:
		model = filter_region(model, comunidad)
	else:
		model = filter_province(model, provincia)

	model = filter_beach(model, playa)
	model = filter_mountain(model, montana)
	model = filter_health(model, salud)
	model = filter_education(model, educacion)
	model = filter_population(model, poblacion)
	model = filter_twinter(model, tinvierno)
	model = filter_tsummer(model, tverano)
	model = filter_elevation(model, altitud)
	model = filter_distance(model, distancia)
	model = filter_incomes(model, renta)
	model = filter_connectivity(model, cobertura)
	model = filter_nature(model, naturaleza)

	if len(model) == 0:
		response = {}
		response["codigo_ine"] = "00000"
		return response

	else:
		suggestion = model.head(1)
		#suggestion = model.sample()
	
		response = {}
		response["codigo_ine"] = suggestion["codigo_ine"].astype(str).values[0]
		response["municipio"] = suggestion["municipio_nombre_humano"].astype(str).values[0]
		response["provincia"] = suggestion["provincia"].astype(str).values[0]
		return response
