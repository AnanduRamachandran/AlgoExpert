
def twoNumberSum(array, targetSum):
	num = {}
	for element in array:
		possiblePair = targetSum - element 
		if possiblePair in num :
			return [possiblePair, element]
		else:
			num[element] = True
	
	return []