# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-1
def knapsack_problem(weights, values, constraint):
  dp = [[0] * (constraint + 1) for _ in range(len(values))]
  if not values:
    return 0
  
  for i in range(len(values)):
    for j in range(constraint + 1):
      if weights[i] > j:
        dp[i][j] = dp[i - 1][j]
      else:
        dp[i][j] = max([dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i]])
  return dp[-1][-1]

print(knapsack_problem([10, 20, 30], [60, 100, 120], 50))
