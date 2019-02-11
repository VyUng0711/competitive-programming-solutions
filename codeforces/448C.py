# http://codeforces.com/problemset/problem/448/C

# Painting:
# min_strokes = min(min_left, min_right)

def divide_and_conquer(l, r):
  min_strokes = a[l]
  for i in range(l + 1, r + 1):
    min_strokes = min(min_strokes, a[i])
    
  ans = min_strokes
  pre = l
  for i in range(l, r + 1):
    a[i] -= min_strokes
    if a[i] == 0:
      ans += divide_and_conquer(pre, i - 1)
      pre = i + 1
  if pre <= r:
    ans += divide_and_conquer(pre, r)
  return min(ans, r - l + 1)


n = int(input())
a = list(map(int, input().split()))
print(divide_and_conquer(0, n - 1))


