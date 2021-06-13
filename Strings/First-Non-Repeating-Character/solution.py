def firstNonRepeatingCharacter(string):
	count ={}
	maximum= len(string) + 1
	for i, element in enumerate(string):
		if element in count:
			count[element] += 1
		else:
			count[element] = 1
	
			
	for i, element in enumerate(string):
		if count[element] == 1:
			return i
	return -1
		