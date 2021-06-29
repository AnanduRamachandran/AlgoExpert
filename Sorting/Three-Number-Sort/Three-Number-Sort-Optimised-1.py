def threeNumberSort(array, order):
	first = order[0]
	last = order[2]
	firstIdx = 0
	lastIdx = len(array)-1
	for i in range(len(array)):
		if array[i] == first:
			swap(i, firstIdx, array)
			firstIdx += 1
	for i in reversed(range(0, len(array))):
		if array[i] == last:
			swap(i, lastIdx, array)
			lastIdx -= 1
	return array
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]