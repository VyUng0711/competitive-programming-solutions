# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
def find_lcs(a, b):
  dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
  for i in range(0, len(a)):
    for j in range(0, len(b)):
      if a[i] == b[j]:
        dp[i + 1][j + 1] = dp[i][j] + 1
      else:
        dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
  return dp[i + 1][j + 1]

