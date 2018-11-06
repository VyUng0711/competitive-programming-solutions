# https://leetcode.com/problems/word-break/description/

# DP using 2D caching

class Solution:
    def wordBreak(self, s, wordDict):
        wordDict = {x for x in wordDict}
        dp = [[False] * len(s) for _ in range(len(s))]
        for l in range(1, len(s) + 1):
            for i in range(0, len(s) - l + 1):
                j = i + l - 1
                sub_str = s[i: j + 1] 
                if sub_str in wordDict:
                    dp[i][j] = True
                    continue
                    
                for k in range(i + 1, j + 1):
                    if dp[i][k - 1] and dp[k][j]:
                        dp[i][j] = True
                        break
                        
        return dp[0][len(s) - 1]

# DP using 1D caching

class Solution:
    def wordBreak(self, s, wordDict):
        wordDict = {x for x in wordDict}
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]
    

