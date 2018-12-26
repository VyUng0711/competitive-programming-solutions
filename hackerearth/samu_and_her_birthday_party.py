# https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/samu-and-her-birthday-party-1/

# Method 1:
def count_dish(i, m):
  # Base case
  if i == n:
    return 0
  # Already visited this state:
  if dp[i][m] != -1:
    return dp[i][m]
  res = n
  for k in range(len(s[i])):
    if s[i][k] == '1':
      if m & (1 << k):
        # This plate is already counted, move to the next person
        res = min(res, count_dish(i + 1, m))
      else:
        # Count this plate in, move to the next person
        res = min(res, 1 + count_dish(i + 1, m | (1 << k)))
  dp[i][m] = res
  return res

num_test = int(input())
for t in range(num_test):
  n, k = map(int, input().split())
  s = []
  for i in range(n):
    s.append(input())
  dp = [[-1 for i in range(2 ** 10)] for j in range(500)]
  print(count_dish(0, 0))
  

# Method 2:

num_test = int(input())
for t in range(num_test):
  n, k = map(int, input().split())
  friends = []
  for i in range(n):
    friends.append(int(input(), 2))

  # print(friends)
  # mask = []
  # for i in range(n):
  #   a = 0
  #   for j in range(k):
  #     if friends[i][j] == '1':
  #       a = a | (1 << (k - 1 - j))
  #   mask.append(bin(a)[2:])
  # print(mask)

  # start from counting all dishes into the menu.
  ans = k
  for i in range(1, 1 << k):
    print(i)
    possible = True
    for j in range(n):
      if friends[j] & i == 0:
      # if mask[j] & i == 0:
        possible = False

    if possible:
      counter = 0
      for m in range(k):
        if (1 << m) & i:
          counter += 1
      ans = min(ans, counter)
  print(ans)

# Shorter:
num_test = int(input())
# print(num_test)
# O(num_test * 2 ^ k * (n + k))
for t in range(num_test): # O(num_test)
  n, k = map(int, input().split())
  friends = []
  for i in range(n): # O(n)
    friends.append(int(input(), 2))
  res = k
  for i in range(2 ** k): # O(2 ^ k)
    ok = True
    for j in friends: # O(n)
      if j & i == 0:
        ok = False
    if ok:
      bin_i = bin(i)[2:]
      count = 0
      for k in range(len(bin_i)):  # O(k)
        if bin_i[k] == '1':
          count += 1
      res = min(res, count)
  print(res)
