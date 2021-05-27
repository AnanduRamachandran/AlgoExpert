def isMonotonic(array):
    i , d = True , True 
	
	for j in range (len(array)-1):
		if i or d :
			if array[j] > array[j+1]:
				i = False
			elif array[j] < array[j+1]:
				d = False
	return i or d