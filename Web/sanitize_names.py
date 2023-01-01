#!/usr/bin/python

import re
import re
from unicodedata import normalize

def make_url_name(name):
	name = name.replace("'", "")
	name = name.split("(")[0]
	name = name.lower()
	name = re.sub(
		r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+",
		r"\1",
		normalize("NFD", name),
		0,
		re.I
	)
	name = normalize('NFC', name)
	name = name.replace(" ", "-")
	name = name.replace("ñ", "n")
	return name