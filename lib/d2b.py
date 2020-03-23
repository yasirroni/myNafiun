import math

def d2b(arr, length = 1):
	"""Convert a binary list to a positive integer list. Works with more than one row input."""
	if isinstance(arr, int):
		return _d2b(arr, length)

	result = []
	for item in arr:
		result.append(_d2b(item, length))
	return result

def _d2b(inp, length = 1):
	if inp==0:
		return [0]
	
	binData = []
	nbin = int(math.floor(math.log(inp, 2) + 1)) #compute required length
	for i in range(0, nbin):
		binData.append(inp >> i & 0b1) #bit shift then extract lsb
	binData.reverse()

	result = [0] * (length - nbin)
	result.extend(binData)
	return result