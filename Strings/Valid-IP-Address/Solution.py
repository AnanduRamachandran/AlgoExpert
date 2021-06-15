def validIPAddresses(string):
	ipAddress = []
	
	for i in range(1, min(len(string), 4 )):
		currentIPAddressParts = ['', '', '', '']
		
		currentIPAddressParts[0] = string[:i]
		if not valid(currentIPAddressParts[0]):
			continue
		for j in range(i+1, min(len(string), i + 4)):
			
			currentIPAddressParts[1] = string[i:j]
			if not valid(currentIPAddressParts[1]):
				continue
				
			for k in range(j+1, min(len(string), j + 4)):
				
				currentIPAddressParts[2] = string[j:k]
				currentIPAddressParts[3] = string[k:]
				
				if valid(currentIPAddressParts[2]) and  valid(currentIPAddressParts[3]):
					ipAddress.append('.'.join(currentIPAddressParts))
					
	return ipAddress
				
			
def valid(value):
	intValue = int(value)
	if intValue > 255:
		return False
	return len(value)== len(str(intValue))