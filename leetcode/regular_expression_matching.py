# https://leetcode.com/problems/regular-expression-matching/description/

class Solution(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        dp[0][0] = True
        for i in range(1, len(dp[0])):
            if pattern[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        for i in range(1, len(text) + 1):
            for j in range(1, len(pattern) + 1):
                if pattern[j - 1] == '.' or pattern[j - 1] == text[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if pattern[j - 2] == "." or pattern[j - 2] == text[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    dp[i][j] = False
        return dp[len(text)][len(pattern)]
        
