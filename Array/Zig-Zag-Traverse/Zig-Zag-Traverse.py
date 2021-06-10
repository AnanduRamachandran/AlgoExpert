def zigzagTraverse(array):
    row, col = 0, 0 
	height = len(array) -1 
	width = len(array[0]) - 1
	out = []
	goingDown = True 
	while not isOutOfBounds(row, height, col, width):
		out.append(array[row][col])
		if goingDown:
			if row == height or col == 0:
				goingDown = False
				if row == height:
					col += 1
				else:
					row +=1
			else:
				row += 1
				col -= 1
		else:
			if row == 0 or col == width:
				goingDown = True
				if col == width:
					row += 1
				else :
					col += 1
			else:
				row -= 1
				col +=1
	return out
		
def isOutOfBounds(row, height, col, width):
	if row > height or col > width :
		return True
	