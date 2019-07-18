r'''
Given an array of length N, swap every pair of alternate elements in the array.
You don't need to print or return anything, just change in the input array itself.
Input Format :

Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces

Output Format :

Elements after swapping, separated by space.

Sample Input 1:

6
9 3 6 12 4 32

Sample Output 2 :

3 9 12 6 32 4

Sample Input 1:

9
9 3 6 12 4 32 5 11 19

Sample Output 2 :

3 9 12 6 32 4 11 5 19

'''
def swapAlternate(arr):
	size = len(arr)
	for i in range(0, size - 1, 2):
		arr[i], arr[i + 1] = arr[i + 1], arr[i] 

n = int(input())
arr = [int(x) for x in input().split()]
swapAlternate(arr)
for i in range(n):
	print(arr[i], end = " ")
