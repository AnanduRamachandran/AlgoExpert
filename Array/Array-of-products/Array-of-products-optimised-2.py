def arrayOfProducts(array):
    new = [1] * len(array)
	product = 1
	for i in range(len(array)):
		new[i] = product
		product = product * array[i]
	product = 1
	for i in reversed(range(len(array))):
		new[i] = new[i] * product
		product = product * array[i]
	
	return new