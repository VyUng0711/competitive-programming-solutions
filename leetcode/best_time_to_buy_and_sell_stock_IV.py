# Time limit exceeded:
class Solution(object):
    def maxProfit(self, k, prices):
        if not prices or k == 0:
            return 0
        
        dp = [[0] * len(prices) for _ in range(k + 1)]
        for i in range(k + 1):
            for j in range(len(prices)):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    max_profit = dp[i][j - 1]
                    for m in range(j):
                        max_profit = max(max_profit, prices[j] - prices[m] + dp[i - 1][m])
                    dp[i][j] = max_profit
                    
        return dp[-1][-1]

# Faster solution, but more memory required:
class Solution(object):
    def maxProfit(self, k, prices):
        if not prices or k == 0:
            return 0
        
        dp = [[0] * len(prices) for _ in range(k + 1)]
        for i in range(k + 1):
            max_diff = -float('inf')
            for j in range(len(prices)):
                # if i == 0 or j == 0:
                #     dp[i][j] = 0
                # else:
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])
                          
                    
        return dp[-1][-1]
        
