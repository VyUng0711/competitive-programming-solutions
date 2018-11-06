# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

# Greedy algorithm:
class Solution(object):
    def maxProfit(self, prices):
        i = 0
        sum_profit = 0
        peak = 0
        valley = 0
        while i < len(prices) - 1:
            
            while i < len(prices) - 1 and prices[i + 1] < prices[i]:
                i += 1
            this_valley = prices[i]
            
            while i < len(prices) - 1 and prices[i + 1] >= prices[i]:
                i += 1
            this_peak = prices[i]
            
            sum_profit += this_peak - this_valley
            print(sum_profit)
        return sum_profit
                


