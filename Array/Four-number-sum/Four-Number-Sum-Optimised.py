def fourNumberSum(array, targetSum):
	table={}
	out = []
    for i in range(1, len(array) - 1):
		for j in range(i+1, len(array)):
			requiredSum = targetSum - (array[i] + array[j])
			if requiredSum in table :
				for pairs in table[requiredSum]:
					out.append( pairs + [array[i],array[j]])
		for k in reversed(range(0, i)):
			tableKey = array[i] + array[k]
			if tableKey not in table:
				table[tableKey] = [[array[i], array[k]]]
			else:
				table[tableKey].append([array[i], array[k]])
	return out
					