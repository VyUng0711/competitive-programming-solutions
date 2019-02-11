# https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3584


# Get half sum
# Get all the subset that sum to the smallest above half sum

def recurse(cur, indx, sum_so_far):
  global min_diff
  if sum_so_far >= half:
    min_diff = min(abs(sum_so_far - (total - sum_so_far)), min_diff)
    return
  for i in range(indx, m):
    cur.append(coins[i])
    recurse(cur, i + 1, sum_so_far + coins[i])
    cur.pop()
  
# DP SOLUTION:
def dp(coins):
  res = [0] * (25000 + 10)
  for i in range(m):
    for j in range(half, coins[i] - 1, -1):
      res[j] = max(res[j], res[j - coins[i]] + coins[i])
  return total - 2 * res[half]



num_test = int(input())
for t in range(num_test):
  m = int(input())
  coins = list(map(int, input().split()))
  total = sum(coins)
  half = total // 2
  # min_diff = float('inf')
  # recurse([], 0, 0)
  # print(min_diff)
  print(dp(coins))



# ANOTHER INTERSTING SOLUTION USING BACKTRACKING WITH SMALLER COMPLEXITY:

# divide by half. each half find every subset 

# A = set of subsets of the left (2 ^ (m/2))
# B = ... right (2 ^  (m / 2))


# a in A # O(2 ^ (m / 2))
# find b in B: sum(a) + sum(b) ~ half # O(2 ^ (m / 2)) --> O(log 2 ^ (m/2)) --> O(m/2)

# --> binary search

# -> O(m/2 * 2 ^ (m/2))


import copy
import bisect
def get_subset(array):
  res = []
  def recurse(cur, indx):
    res.append(copy.deepcopy(cur))
    if indx == len(array):
      return

    for i in range(indx, len(array)):
      cur.append(array[i])
      recurse(cur, i + 1)
      cur.pop()

  recurse([], 0)

  return res


num_test = int(input())
for t in range(num_test):
  m = int(input())
  coins = list(map(int, input().split()))
  total = sum(coins)
  half = total // 2

  left_a = coins[:m//2]
  right_a = coins[m//2:]

  left = get_subset(left_a)
  right = get_subset(right_a)


  sum_left = [sum(x) for x in left]
  sum_right = [sum(x) for x in sorted(right)]

  min_diff = float('inf')
  for k in sum_left:
    target_indx = bisect.bisect_left(sum_right, half - k)
    if target_indx > len(sum_right) - 1:
      target_indx = len(sum_right) - 1

    target = sum_right[target_indx]

    this_diff = abs(2 * (k + target)  - total)
    min_diff = min(this_diff, min_diff)

  print(min_diff)
    
