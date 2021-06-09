def largestRange(array):
	bestRange = []
	table = {}
	longestRange = 0
	for nums in array:
		table[nums] = True
	for nums in array:
		if not table[nums]:
			continue
		right = nums + 1
		left = nums - 1
		length = 1
		while right in table :
			table [right] = False
			right += 1
			length += 1
		while left in table :
			table [left] = False
			left -= 1
			length += 1
		if length > longestRange :
			bestRange = [ left + 1 , right - 1]
			longestRange = length
	return bestRange
			