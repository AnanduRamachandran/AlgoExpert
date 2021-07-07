def shiftedBinarySearch(array, target):
    left = 0
	right = len(array) - 1
	while left <= right:
		middle = (left + right) // 2
		potentialMatch = array[middle]
		leftNum = array[left]
		rightNum = array[right]
		if target == potentialMatch:
			return middle 
		elif leftNum <= potentialMatch:
			if target < potentialMatch and target >= leftNum:
				right = middle - 1
			else:
				left = middle + 1
		else:
			if target > potentialMatch and target <= rightNum: 
				left = middle + 1
			else:
				right = middle - 1
	return -1