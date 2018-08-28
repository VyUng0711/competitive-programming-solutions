# http://codeforces.com/problemset/problem/68/B
n, k = map(int, input().split())
energy = list(map(int, input().split()))

def match(x):
  left, right = 0, 0
  for i in range(n):
    if energy[i] < x:
      left += x - energy[i]
    else:
      right += energy[i] - x
  return right - (right * k)/ 100 >= left

left = 0
right = 1000

# len = 1000
# 1000 / 2 ^ k <= 10 ^ -6
# 2 ^ k >= 10 ^ 9
# k >= log2(10 ^ 9) ~ 31
# O(31N) ~ O(N)

while right - left > 0.000001:
  mid = (left + right) / 2
  if match(mid):
    left = mid
  else:
    right = mid

print (left)
