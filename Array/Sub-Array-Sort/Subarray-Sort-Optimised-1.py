def subarraySort(array):
	smallest = max(array)
	minpos=0
	maximum = min(array)
	maxpos = 0
	out = []

	for i in range(len(array)-1):
		if array[i] > array[i+1] :
			if array[i+1] <= smallest:
				smallest = array[i+1]
				minpos = i+1
	for i in range(len(array)-1):
		if array[i+1] < array[i]:
			if array[i] >= maximum:
				maximum = array[i]
				maxpos = i
	for i in range (len(array)):
		if array[i] > smallest:
			out.append(i)
			break
	for i in reversed(range(len(array))):
		if array[i] < maximum:
			out.append(i)
			break
	if len(out) != 2:
		return [-1, -1]
	return out