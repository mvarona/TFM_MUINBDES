from random import randrange

def get_random_background():
	names = []
	backgrounds = []
	authors = []
	urls = []

	names.append("Barcelona")
	names.append("Playa española")
	names.append("Granada")
	names.append("León")
	names.append("Málaga")
	names.append("Ronda, Málaga")
	names.append("Sevilla")
	names.append("España")
	names.append("España")
	names.append("España")
	names.append("España")
	names.append("España")
	names.append("Torimbia, Asturias")

	backgrounds.append("barcelona.jpg")
	backgrounds.append("beach.jpg")
	backgrounds.append("granada.jpg")
	backgrounds.append("leon.jpg")
	backgrounds.append("malaga.jpg")
	backgrounds.append("ronda.jpg")
	backgrounds.append("sevilla.jpg")
	backgrounds.append("spain_1.jpg")
	backgrounds.append("spain_2.jpg")
	backgrounds.append("spain_3.jpg")
	backgrounds.append("spain_4.jpg")
	backgrounds.append("spain_5.jpg")
	backgrounds.append("torimbia.jpg")

	authors.append("qute")
	authors.append("bercus")
	authors.append("villen")
	authors.append("laser")
	authors.append("metanormal")
	authors.append("wax115")
	authors.append("oneg")
	authors.append("schlitzy")
	authors.append("gerhard")
	authors.append("mancastro")
	authors.append("suzannekra")
	authors.append("gerhard")
	authors.append("titochavi")

	urls.append("https://www.freeimages.com/es/photo/barcelona-1-1561613")
	urls.append("https://www.freeimages.com/es/photo/beach-in-spain-1404075")
	urls.append("https://www.freeimages.com/es/photo/granada-1452483")
	urls.append("https://www.freeimages.com/es/photo/leon-catedral-spain-2-1456181")
	urls.append("https://www.freeimages.com/es/photo/spain-malaga-inland-nature-1530787")
	urls.append("https://www.freeimages.com/es/photo/ronda-spain-7-1501670")
	urls.append("https://www.freeimages.com/es/photo/evening-in-sevilla-1542567")
	urls.append("https://www.freeimages.com/es/photo/spain-6-1505181")
	urls.append("https://www.freeimages.com/es/photo/spain-3-1561688")
	urls.append("https://www.freeimages.com/es/photo/spain-sea-side-1390369")
	urls.append("https://www.freeimages.com/es/photo/river-in-spain-1385181")
	urls.append("https://www.freeimages.com/es/photo/spain-1-1505177")
	urls.append("https://www.freeimages.com/es/photo/torimbia-beach-asturias-spain-1390778")
	
	num = randrange(len(backgrounds))

	return names[num], backgrounds[num], authors[num], urls[num]