 https://leetcode.com/problems/coin-change-2/

class Solution:
    def change(self, amount, coins):
        # There is always way to get 0:
        if amount == 0:
            return 1
        else:
            if not coins:
                return 0

        dp = [[1] + [0] * amount for _ in range(len(coins))]
        for i in range(len(coins)):
            for j in range(1, amount + 1):
                if i >= 1:
                    without_this_coin = dp[i - 1][j]
                else:
                    without_this_coin = 0
                if j >= coins[i]:
                    with_this_coin = dp[i][j - coins[i]]
                else:
                    with_this_coin = 0
                dp[i][j] = without_this_coin + with_this_coin
        return dp[-1][-1]
                
     
