def findThreeLargestNumbers(array):
	a = b = c = float("-inf")
	for i in range(len(array)):
		if array[i] > a:
			if array[i] > b:
				if array[i] > c:
					a = b
					b = c
					c = array[i] 
				else:
					a = b
					b = array[i]
			else:
				a = array[i]
	return [a,b,c]
				