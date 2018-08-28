# https://leetcode.com/problems/sort-colors/discuss/
def dutch_flag(pivot_index, A):
	pivot = A[pivot_index]
	smaller = 0
	for i in range(len(A)):
		if A[i] < pivot:
			A[i], A[smaller] = A[smaller], A[i]
			smaller += 1
	larger = len(A) - 1
	for j in reversed(range(len(A))):
		if A[j] > pivot:
			A[j],A[larger] = A[larger], A[j]
			larger -=1
	return A
test = [3,5,8,4,0,10,1,2,11]
print (dutch_flag(3,test))