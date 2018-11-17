class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
    
        up = 0
        down = len(matrix) - 1
        row = None
        while up + 1 < down:
            mid = (up + down) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                down = mid - 1
            else:
                up = mid
         
        if matrix[down][0] <= target:
            row = matrix[down]
        elif matrix[up][0] <= target:
            row = matrix[up]
        
        if not row:
            return False
        # print(row)
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            if row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
