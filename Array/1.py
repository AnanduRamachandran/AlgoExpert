# Write a function that takes in a non-empty array of Integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order.

def sortedSquaredArray(array):
    # Write your code here.
    x=-1
	a=0
	b=-1
	arr=[0 for _ in array]
	for i in range (len(array)):
		if abs(array[a])>=abs(array[b]):
			temp=(array[a])**2
			arr[x]=temp
			a=a+1
		else:
			temp=(array[b])**2
			arr[x]=temp
			b=b-1
		x=x-1
			
    return arr