def isPalindrome(string):
	right = len(string) - 1
	left = 0
    for i in range(round((len(string))/2)):
		if string[right] != string[left]:
			return False
		left += 1
		right -= 1
	return True