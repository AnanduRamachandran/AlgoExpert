def firstDuplicateValue(array):
	low = float('inf')
	for i in range(len(array)):
		for j in range(i+1, len(array)):
			if i != j :
				if j < low and array[i]==array[j]:
					low = j
	if low == float('inf') or len(array) == 1:
		return -1
	else:
		return array[low]

