# https://leetcode.com/problems/minimum-path-sum/description/
class Solution(object):
    def minPathSum(self, grid):
        if not grid:
            return 0
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:      
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[-1][-1]
