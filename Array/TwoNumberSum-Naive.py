
def twoNumberSum(array, targetSum):
    # Write your code here.
	new = []
	for i in range (len(array)):
		a = -1
		for j in range (len(array)-i-1):
			if array[i] + array[a] == targetSum :
				new.extend([array[i],array[a]])
			a-=1
	return new