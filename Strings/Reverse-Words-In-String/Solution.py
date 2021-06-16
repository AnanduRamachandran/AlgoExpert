def reverseWordsInString(string):
	length = len(string)
	out = []
	count = 0
    for i in range(length-1, -1, -1):
		if i == 0:
			if count > 0:
				for j in range(i , i + (count +1)):
					out.append(string[j])
			else:
				out.append(string[i])
		elif string[i] ==" ":
			if count > 0:
				for j in range(i +1, i + (count +1)):
					out.append(string[j])
			out.append(" ")
			count = 0
		else:
			count += 1
	return ''.join(out)