def tournamentWinner(competitions, results):
    # Write your code here.
	winner = {}
	for ind, match in enumerate(competitions):
		currentWinner = match[abs((results[ind])-1)]
		if currentWinner in winner:
			winner[currentWinner] += 3
		else :
			winner[currentWinner] = 3
			
    return max(winner, key=winner.get)
