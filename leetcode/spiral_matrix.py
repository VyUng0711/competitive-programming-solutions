# https://leetcode.com/problems/spiral-matrix/description/

class Solution:
    def spiralOrder(self, matrix):
        
        if len(matrix) == 0:
            return []
        
        start_i = 0
        end_i = len(matrix) - 1
        start_j = 0
        end_j = len(matrix[0]) - 1
        
        result = []
        
        while len(result) < len(matrix) * len(matrix[0]) and start_i <= end_i and start_j <= end_j:
            #Right
            for j in range(start_j, end_j):
                if len(result) < len(matrix) * len(matrix[0]):
                    result.append(matrix[start_i][j])
            #Down
            for i in range(start_i, end_i):
                if len(result) < len(matrix) * len(matrix[0]):
                    result.append(matrix[i][end_j])
            #Left
            for j in range(end_j, start_j, -1):
                if len(result) < len(matrix) * len(matrix[0]):
                    result.append(matrix[end_i][j])
            #Up
            for i in range(end_i, start_i, -1):
                if len(result) < len(matrix) * len(matrix[0]):
                    result.append(matrix[i][start_j])
            start_i += 1
            end_i -= 1
            start_j += 1
            end_j -= 1
            
            # print(result)
             
        if len(matrix) % 2 == 1 and len(matrix[0]) % 2 == 1 and len(matrix) == len(matrix[0]):
            result.append(matrix[(len(matrix) - 1) // 2][(len(matrix[0]) - 1) // 2])
        return result


