# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        num_layer = n // 2
        for l in range(num_layer):
            start = l
            end = n - l - 1
            for i in range(start, end):
                offset = i - start
                # save top
                top = matrix[start][i]
                # move left to top
                matrix[start][i] = matrix[end - offset][start]
                # move bottom to left
                matrix[end - offset][start] = matrix[end][end - offset]
                # move right to bottom
                matrix[end][end - offset] = matrix[i][end]
                # assign top to right
                matrix[i][end] = top
