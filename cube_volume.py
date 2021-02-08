def cube(x):
	if (str(x).isdecimal() and float(x) > 0.0):
		return x * x * x
	else:
		return -1
