# DP: find maximum sum non-empty submatrix:
def find_maximum_sum_subarray(a):
  dp = [None] * len(a)
  dp[0] = a[0]
  global_max = a[0]
  for i in range(1, len(a)):
    dp[i] = max(a[i], dp[i - 1] + a[i])
    global_max = max(global_max, dp[i])
  # print(dp)
  return global_max


print(find_maximum_sum_subarray([-2, -3, 4, -1, -2, 1, 5, -3]))

def find_maximum_sum_submatrix(m):
  global_max = m[0][0]
  for left in range(len(m[0])):
    temp = [0] * len(m)
    for right in range(left, len(m[0])):
      for i in range(len(m)):
        temp[i] += m[i][right]
      cur_max = find_maximum_sum_subarray(temp)
      global_max = max(cur_max, global_max)
      
  return global_max


print(find_maximum_sum_submatrix([[2, 1, -3, -4, 5],
                           [0, 6, 3, 4, 1],
                           [2, -2, -1, 4, -5],
                           [-3, 3, 1, 0, 3]]))
      

