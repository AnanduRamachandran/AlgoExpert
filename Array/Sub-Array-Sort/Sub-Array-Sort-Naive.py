def subarraySort(array):
    new = []
	array1 = sorted(array)
	for i in range(len(array)):
		if array[i] != array1[i]:
			new.append(i)
			break 
	for i in reversed(range(len(array))):
		if array[i] != array1[i]:
			new.append(i)
			break
	if len(new) != 2:
		return [-1,-1]
	else :
		return new