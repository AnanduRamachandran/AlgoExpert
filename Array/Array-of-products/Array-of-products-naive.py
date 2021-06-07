def arrayOfProducts(array):
	newArray = []
	for i in range(len(array)):
		product = 1
		for j in range(len(array)):
			if i != j:
				product = product*array[j]
		newArray.append(product)
	return newArray
			