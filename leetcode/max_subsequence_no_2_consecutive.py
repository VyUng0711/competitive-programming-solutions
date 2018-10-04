# https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/

def subs_with_no_2_consecutive(a):
  dp = [None] * (len(a) + 2)
  dp[-2] = 0
  dp[-1] = 0
  for i in range(len(a)):
    dp[i] = max(dp[i - 1], dp[i - 2] + a[i])
  return dp[i]
