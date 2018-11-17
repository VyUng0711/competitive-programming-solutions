# https://leetcode.com/problems/set-matrix-zeroes/

# Brute force
# Time: O(n * m * (m + n))
# Space: O(1)

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix[0])):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 'x'
                    for h in range(len(matrix)):
                        if matrix[h][j] != 0:
                            matrix[h][j] = 'x'
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'x':
                    matrix[i][j] = 0

# Optimized:
# Time: O(n * m)
# Space: O(1)

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        first_row = False
        first_col = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col = True
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                first_row = True
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
                    
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        if first_row:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if first_col:
            for j in range(len(matrix)):
                matrix[j][0] = 0
