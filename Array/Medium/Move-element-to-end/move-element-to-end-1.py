def moveElementToEnd(array, toMove):
	point = 0
	for i in range (len(array)):
		if array[i] != toMove :
			array[i], array[point] = array[point], array[i]
			point += 1
	return array