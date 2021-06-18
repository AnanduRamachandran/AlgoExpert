def minimumCharactersForWords(words):
	count = {}
	out = []
    for i in range(len(words)):
		word = words[i]
		letterCount = {}
		for letter in word:
			if letter in count:
				if letter in letterCount:
					letterCount[letter] +=1
					if letterCount[letter] > count[letter]:
						count[letter] += 1
				else:
					letterCount[letter] = 1
			else:
				count[letter] = 1
				letterCount[letter] = 1
				
	for i in count:
		while count[i] > 0:
			out.append(i)
			count[i] -= 1
	return out