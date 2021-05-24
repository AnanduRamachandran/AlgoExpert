def tournamentWinner(competitions, results):
    # Write your code here.
	win , a , previous_count = [] , 0 , 0
	
	for i in results:
		p=competitions[a]
		if i > 0:
			win.append(p[0])
		else:
			win.append(p[1])
		a += 1
	for winner in win:
		if previous_count < win.count(winner):
			previous_count = win.count(winner)
			winner1 = winner
    return winner1