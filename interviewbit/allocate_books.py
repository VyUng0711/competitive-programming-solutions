# https://www.interviewbit.com/problems/allocate-books/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        if len(A) < B:
            return -1
        def find_min_num_student(A, max_num_pages):
            min_num_student = 1
            cur = 0
        
            for i in range(len(A)):
                if A[i] > max_num_pages:
                    return float('inf')
                if cur + A[i] > max_num_pages:
                    min_num_student += 1
                    cur = A[i]
                else:
                    cur += A[i]
            return min_num_student
            
        left = 0
        right = sum(A)
        min_num_pages = -1
        while left <= right: 
            mid = (left + right) // 2
            if find_min_num_student(A, mid) > B:
                left = mid + 1
            else:
                min_num_pages = mid
                right = mid - 1
          
        return min_num_pages
        

