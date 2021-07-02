def threeNumberSort(array, order):
	firstIdx, secondIdx, thirdIdx = 0, 0, len(array)-1
	
	while secondIdx <= thirdIdx:
		value = array[secondIdx]
		
		if value == order[0]:
			array[secondIdx], array[firstIdx] = array[firstIdx], array[secondIdx]
			secondIdx += 1
			firstIdx += 1
		elif value == order[1]:
			secondIdx += 1
		else:
			array[secondIdx], array[thirdIdx] = array[thirdIdx], array[secondIdx]
			thirdIdx -= 1
	return array
