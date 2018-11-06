class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        max_profit = 0
        min_buy_so_far = float('inf')
        for price in prices:
            max_profit = max(price - min_buy_so_far, max_profit)
            min_buy_so_far = min(min_buy_so_far, price)
        return max_profit
            

 
