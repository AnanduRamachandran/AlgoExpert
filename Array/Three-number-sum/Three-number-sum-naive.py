def threeNumberSum(array, targetSum):
    new=[]
	length = len(array)
	for i in range (length-2):
		for j in range (i+1, length-1):
			for k in range(j+1, length):
				if array[i]+array[j]+array[k]==targetSum:
					sub = [array[i], array[j], array[k]]
					sub.sort()
					new.append(sub)
	new.sort()
	return new