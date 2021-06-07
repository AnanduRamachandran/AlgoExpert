def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key =lambda x: x[0] )
	
	currentInterval = sortedIntervals[0]
	mergedIntervals = []
	mergedIntervals.append(currentInterval)
	for i in sortedIntervals:
		if mergedIntervals[-1][1] >= i[0]:
			mergedIntervals[-1][1] = max(i[1] , mergedIntervals[-1][1])
		else:
			mergedIntervals.append(i)
	return mergedIntervals