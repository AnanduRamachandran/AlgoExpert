def caesarCipherEncryptor(string, key):
	new = 0 
	array = []
	for i in string:
		value = ord(i)
		key = key % 26
		if (value + key)  > 122:
			new = ((value + key) % 122 ) + 96
		else:
			new = value + key
		array.append(chr(new))
		
	return ''.join(array)
