# No obstacle: https://leetcode.com/problems/unique-paths/description/
class Solution:
    def uniquePaths(self, m, n):
        dp = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    if i == 0:
                        dp[i][j] = dp[i][j - 1]
                    elif j == 0:
                        dp[i][j] = dp[i - 1][j]
                    else: 
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
        """
        :type m: int
        :type n: int
        :rtype: int
        """

# With obstacles:
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        if obstacleGrid[0][0] == 1:
            return 0
        
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        if i == 0:
                            dp[i][j] = dp[i][j - 1]
                        elif j == 0:
                            dp[i][j] = dp[i - 1][j]
                        else: 
                            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
