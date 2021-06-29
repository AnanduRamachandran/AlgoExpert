def threeNumberSort(array, order):
	isSorted = False
    while not isSorted:
		isSorted = True
		for i in range(0, len(array)-1):
			if notInOrder(i, i+1, array, order):
				swap (i, i+1, array)
				isSorted = False
	return array
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
def notInOrder(i, j, array, order):
	return ((array[i]==order[1] and array[j]==order[0]) or (array[i]==order[2] and (array[j]==order[1] or array[j] == order[0])))