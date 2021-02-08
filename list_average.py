def list_average(items):
	if (len(items) > 0):
		for x in items:
			if (not str(x).isdecimal()): return None

		items_sum = 0
		
		for x in items:
			items_sum += x
			
		return items_sum / len(items)
	else:
		return None
		
