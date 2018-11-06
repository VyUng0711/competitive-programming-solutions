# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

class Solution(object):
    def maxProfit(self, prices):
        before = [0] * (len(prices))
        after = [0] * (len(prices))
        max_profit_before = 0
        max_profit_after = 0
        min_buy_before = float('inf')
        max_sell_after = float('-inf')
        
        for i in range(len(prices)):
            min_buy_before = min(min_buy_before, prices[i])
            max_profit_before = max(max_profit_before, prices[i] - min_buy_before)
            before[i] = max_profit_before
            
            
        for j in range(len(prices) - 1, -1, -1):
            max_sell_after = max(max_sell_after, prices[j])
            max_profit_after = max(max_sell_after - prices[j], max_profit_after)
            after[j] = max_profit_after
            
        max_total = 0
        for k in range(len(prices) - 1):
            max_total = max(max_total, before[k] + after[k])
            
        return max_total


