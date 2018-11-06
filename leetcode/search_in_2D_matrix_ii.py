# https://leetcode.com/problems/search-a-2d-matrix-ii/description/

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        r, c = 0, len(matrix[0]) - 1
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False


