# https://www.geeksforgeeks.org/maximum-subsequence-sum-such-that-no-three-are-consecutive/

def subs_with_no_3_consecutive(a):
  dp = [None] * (len(a) + 3)
  for j in [-3, -2, -1]:
    dp[j] = 0
    
  for i in range(0, len(a)):
    dp[i] = max([dp[i - 1], dp[i - 2] + a[i], dp[i - 3] + a[i - 1] + a[i]])
    
  return dp[i]
