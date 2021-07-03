def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
	for num in array:
		updateLargest(threeLargest, array, num)
	return threeLargest

def updateLargest(threeLargest, array, num):
	if threeLargest[2] is None or num > threeLargest[2]:
		shift(threeLargest, 2, num)
	elif threeLargest[1] is None or num > threeLargest[1]:
		shift(threeLargest, 1, num)
	elif threeLargest[0] is None or num > threeLargest[0]:
		shift(threeLargest, 0, num)
		
def shift(array, idx, num):
	for i in range(idx+1):
		if i == idx:
			array[i] = num
		else:
			array[i] = array[i+1]