# https://leetcode.com/problems/edit-distance/description/

class Solution(object):
    def minDistance(self, word1, word2):
        
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        
        
        for i in range(0, len(word1) + 1):
            for j in range(0, len(word2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + 1
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + 1
                else:
                    if word1[i - 1] == word2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                
        return dp[-1][-1]
                    


