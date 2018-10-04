# https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/
# Method 1: Directly find length of longest palindromic subsequence 
def find_lps(s):

  dp = [[0] * len(s) for _ in range(len(s))]
  
  for k in range(len(s)):
    dp[k][k] = 1
    
  # start from i and end at j
  for i in range(len(s) - 1, -1, -1):
    for j in range(i + 1, len(s)):
      if s[i] == s[j]:
        dp[i][j] = dp[i + 1][j - 1] + 2
      else:
        dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])                                         
  return dp[0][len(s) - 1]



# Method 2: Length of longest palindromic subsequence
# is length of longest common subsequence of the input string and its reverse.
def find_lcs(a, b):
  dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
  for i in range(0, len(a)):
    for j in range(0, len(b)):
      if a[i] == b[j]:
        dp[i + 1][j + 1] = dp[i][j] + 1
      else:
        dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
  return dp[i + 1][j + 1]

def find_lps_using_lcs(s):
  reversed = s[::-1]
  return find_lcs(s, reversed)
print(find_lps_using_lcs(s))
