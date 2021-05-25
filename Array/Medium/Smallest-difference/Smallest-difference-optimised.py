def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
	arrayTwo.sort()
	smallestPair = []
	minimum = float ('inf')
	current = float ('inf')
	idxOne = 0
	idxTwo = 0
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo) :
		current = abs(arrayOne[idxOne]-arrayTwo[idxTwo])
		firstNum = arrayOne[idxOne]
		secondNum = arrayTwo[idxTwo]
		if firstNum < secondNum:
			idxOne += 1
		elif firstNum > secondNum:
			idxTwo += 1
		else:
			return [firstNum , secondNum]
		if current < minimum :
			minimum = current 
			smallestPair = [firstNum , secondNum]
	return smallestPair