def generateDocument(characters, document):
	char = {}
    for i in range(len(characters)):
		if characters[i] in char:
			char[characters[i]] += 1
		else:
			char[characters[i]] = 1
			
	for i in range(len(document)):
		if document[i] not in char:
			return False
		elif char[document[i]] == 0:
			return False
		elif document[i] in char:
			char[document[i]] -= 1
			
	if len(characters) == len(document) and len(document) == 0:
		return True
	
	elif len(characters) == 0:
		return False
	else:
		return True