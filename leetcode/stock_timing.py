# Best time to Buy and Sell Stock I One Time
def maxProfit_1(prices):
  min_price_so_far = float("inf")
  max_profit_so_far = 0
  for p in prices:
    max_profit_so_far = max(p - min_price_so_far, max_profit_so_far)
    min_price_so_far = min(p, min_price_so_far)
  return max_profit_so_far

print(maxProfit_1([7,6,4,3,1]))

# Best Time to Buy and Sell Stock II Multiple Times
def maxProfit_n(prices):
    if len(prices) == 0:
        return 0
    i = 0
    high = prices[0]
    low = prices[0]
    max_profit = 0
    
    while i < len(prices) - 1:
        while i < len(prices) - 1 and prices[i] >= prices[i+1]:
            i+=1
        low = prices[i]
        while i < len(prices) - 1 and prices[i] <= prices[i+1]:
            i+=1
        high = prices[i]
        max_profit += high - low
    return max_profit

# Best Time to Buy and Sell Stock III Exactly Two Times
def maxProfit_2(prices):
    
