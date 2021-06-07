def threeNumberSum(array, targetSum):
	array.sort()
    trip =[]
	for i in range (len(array)-2):
		left = i+1
		right = len(array)-1
		while left < right :
			currentSum = array[i]+array[left]+array[right]
			if currentSum  == targetSum:
				trip.append([array[i], array[left] , array[right]])
				right -= 1
				left +=1
			elif currentSum < targetSum :
				left += 1
			elif currentSum > targetSum :
				right -= 1
	return trip