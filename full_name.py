def full_name(first, last):

	if (first != None and last != None and first != "" and last != ""):
		return str(first) + " " + str(last)
		
	elif (first != None or last != None):
		return str(first) + str(last)
		
	else:
		return ""
