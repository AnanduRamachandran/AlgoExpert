def longestPalindromicSubstring(string):
    start, end = 0, 0
	length = 0
	
	for i in range(len(string)):
		for j in range(i+1, len(string)):
			if string[i] == string[j]:
				if isPal(i, j, string):
					lenNow = (j-i) + 1
					if lenNow > length:
						length = lenNow
						start, end = i, j
	return string[start : end+1]

def isPal(x, y, string):
	left = x
	right = y
	while left < right:
		if string[left] == string[right]:
			left += 1
			right -= 1
		else:
			return False
	return True