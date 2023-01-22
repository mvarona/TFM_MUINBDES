#!/usr/bin/python

# Mario Varona Bueno
# TFM MUINBDES
# 2022
# Returns a decimal number as string

def convert_decimal_numbers(num, roundNumber=True):
	if num == "-":
		return num
	if roundNumber == False:
		num = str(num)
		num = num.replace(".", ",")
		return num
	else:
		num = str(int(float(num)))

	if len(num) == 4:
		before_dot = num[1:]
		after_dot = num[:1]
		num = after_dot + "." + before_dot

	elif len(num) == 5:
		before_dot = num[2:]
		after_dot = num[:2]
		num = after_dot + "." + before_dot

	elif len(num) == 6:
		before_dot = num[3:]
		after_dot = num[:3]
		num = after_dot + "." + before_dot

	elif len(num) == 7:
		before_dot = num[4:]
		after_dot = num[:4]
		num = after_dot + "." + before_dot
		before_dot = num[1:]
		after_dot = num[:1]
		num = after_dot + "." + before_dot

	elif len(num) == 8:
		before_dot = num[5:]
		after_dot = num[:5]
		num = after_dot + "." + before_dot


	return num