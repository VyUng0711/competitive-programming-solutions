# https://www.hackerrank.com/challenges/sansa-and-xor/problem

num_test = int(input())
for t in range(num_test):
  n = int(input())
  a = list(map(int, input().split()))
  if len(a) & 1 == 0:
    print(0)
  else:
    res = a[0]
    for i in range(2, len(a), 2):
      res ^= a[i]
    print(res)


# a[i] 

# 1 2 3

# 2: [1, 2], [1, 2, 3], [2], [2, 3]
# 3: [3], [2, 3], [1, 2, 3]

# n = 3
# (i + 1) * (n - i)
