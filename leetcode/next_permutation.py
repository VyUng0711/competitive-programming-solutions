class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        index = -1
        for i in xrange(len(A) - 2, -1, -1):
            if A[i] < A[i + 1]:
                index = i
                break
        if index == -1:
            A = reversed(A)
            return A

        for j in xrange(len(A) - 1, -1, -1):
            if A[j] > A[index]:
                A[j], A[index] = A[index], A[j]
                break
        A[index + 1:] = reversed(A[index + 1:])
        return A
