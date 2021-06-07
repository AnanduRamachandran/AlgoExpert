def fourNumberSum(array, targetSum):
	nextArray = []
    for i in range(len(array)-3):
		for j in range(i+1,len(array)-2):
			for k in range(j+1, len(array)-1):
				for l in range(k+1, len(array)):
					if array[i]+array[j]+array[k]+array[l] == targetSum:
						nextArray.append([array[i], array[j], array[k], array[l]])
	return nextArray