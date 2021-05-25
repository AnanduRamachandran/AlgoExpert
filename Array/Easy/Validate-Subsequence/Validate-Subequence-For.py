def isValidSubsequence(array, sequence):
	k=0
	
	for i in range(len(array)):
			if k < len(sequence) and array[i] == sequence[k]:
				k += 1
	return k == len(sequence)