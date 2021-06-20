def longestSubstringWithoutDuplication(string):
	table = {}
	startIdx = 0
	longest = [0, 1]
    for i, word in enumerate(string):
		if word in table:
			startIdx = max(startIdx, table[word]+1)
		if longest[1] - longest[0] < i+1 - startIdx:
			longest = [startIdx, i+1]
		table[word] = i
	return string[longest[0] : longest[1]]