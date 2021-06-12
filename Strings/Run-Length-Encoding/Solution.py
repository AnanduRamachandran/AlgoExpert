def runLengthEncoding(string):
    chars = []
	count = 1
	for i in range(1, len(string)):
		currentElement = string[i]
		previousElement = string[i-1] 
		
		if currentElement != previousElement or count == 9:
			chars.append(str(count))
			chars.append(previousElement)
			count = 0
		
		count += 1
		
	chars.append(str(count))
	chars.append(string[len(string)-1])
	
	return ''.join(chars)