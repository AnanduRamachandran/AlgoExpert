def longestPalindromicSubstring(string):
    long = [0,1]
	for i in range(len(string)):
		odd = isPalindrome(string, i - 1, i + 1)
		even = isPalindrome(string, i -1, i)
		longest = max(odd, even, key = lambda x: x[1] - x[0])
		long = max(longest, long, key = lambda x: x[1] - x[0])
	return string[long[0]:long[1]]

def isPalindrome(string, leftIdx, rightIdx):
	while leftIdx >= 0 and rightIdx < len(string):
		if string[leftIdx] != string[rightIdx]:
			break
		rightIdx += 1
		leftIdx -= 1
	return [leftIdx + 1, rightIdx]
