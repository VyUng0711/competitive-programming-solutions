# https://leetcode.com/problems/range-sum-query-2d-immutable/description/

class NumMatrix:

    def __init__(self, matrix):
        if not matrix:
            return 
        
        self.pre = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                self.pre[i + 1][j + 1] = self.pre[i + 1][j] + self.pre[i][j + 1] - self.pre[i][j] + matrix[i][j]
                

    def sumRegion(self, row1, col1, row2, col2):
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        print(self.pre)
        return self.pre[row2][col2] - self.pre[row1 - 1][col2] - self.pre[row2][col1 - 1] + self.pre[row1 - 1][col1 - 1]
    
