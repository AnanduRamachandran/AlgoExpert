def arrayOfProducts(array):
    left = [1] * len(array)
	right = [1] * len(array)
	new = []
    
	product = 1
	for i in range(len(array)):
		left[i] = product 
		product = product * array[i]
		
	product = 1
		
	for i in reversed(range(len(array))):
		right[i] = product 
		product = product * array[i]
	
	for i in range(len(array)):
		new.append(left[i] * right[i])
		
	return new