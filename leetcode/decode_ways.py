# https://leetcode.com/problems/decode-ways/description/
class Solution(object):
    def numDecodings(self, s):
        if not s:
            return 0
        if len(s) == 1:
            if s[0] == '0':
                return 0
            return 1
                
        dp = [0] * len(s)
        dp[0] = (1 if s[0] != '0' else 0)
        dp[-1] = 1
        for i in range(1, len(s)):
            if s[i] != '0':
                if int(s[i - 1: i + 1]) > 26 or s[i - 1] == '0':
                    dp[i] = dp[i - 1]
                else:
                    dp[i] = dp[i - 1] + dp[i - 2]
            else:
                if int(s[i - 1: i + 1]) > 26 or s[i - 1] == '0':
                    return 0
                else:
                    dp[i] = dp[i - 2]
                    
        return dp[-1]
    

