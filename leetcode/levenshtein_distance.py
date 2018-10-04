# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1, word2):
        word1 = " " + word1
        word2 = " " + word2
        dp = [[0] * (len(word1)) for _ in range(len(word2))]
        # print(len(word1))
        # print(len(word2))
        

        for i in range(len(word2)):
            for j in range(len(word1)):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    if word2[i] == word1[j]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = min([dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]]) + 1
                        
        return dp[i][j]
