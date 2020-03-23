"""Convert a binary list to a positive integer list. Works with more than one row input."""
def b2d(inp):
	if isinstance(inp[0], int): #1 dimension
		return _b2d(inp)
	
	result=[] #2 dimensions
	for item in inp:
		result.append(_b2d(item))
	return result

def _b2d(inp):
	result=0
	inp=inp[::-1]
	for col in range(len(inp)):
		if inp[col]==1:
			result=result+2**col
	return(result)
