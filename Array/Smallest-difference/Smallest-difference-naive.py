def smallestDifference(arrayOne, arrayTwo):
	small = float('inf')
	elements = [0, 0]
	for i in range (len(arrayOne)):
		for j in range(len(arrayTwo)):
			new = abs (arrayOne[i] - arrayTwo[j])
			if new < small :
				elements[0] , elements[1] = arrayOne [i], arrayTwo[j]
				small = new
	return elements
			