def subarraySort(array):

    res = [-1,-1]

    minUnsorted = array[0]
    for i in range(len(array)):
        if array[i] < minUnsorted:
            res[1] = i
        else:
            minUnsorted = array[i]


    maxUnsorted = array[-1]
    for i in reversed(range(len(array))):
        if maxUnsorted < array[i]:
            res[0] = i
        else:
            maxUnsorted = array[i]