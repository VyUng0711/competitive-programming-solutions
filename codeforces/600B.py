# http://codeforces.com/problemset/problem/600/B
# Using array
def less_or_equal(a, b):
  # O(nlogn + mlogm)
  sorted_b = sorted([(b[x], x) for x in range(len(b))])
  sorted_a = sorted(a)
  i = 0
  dict = [None]*len(sorted_b)
  # O(n + m)
  for j in range(len(sorted_b)):
    while i < len(sorted_a) and sorted_a[i] <= sorted_b[j][0]:
      i+=1
    dict[sorted_b[j][1]] = i
  print(*dict)


# Using dictionary
def less_or_equal_2(a, b):
  dict = {}
  sorted_b = sorted(b)
  sorted_a = sorted(a)
  i = 0
  for j in range(len(sorted_b)):
    while i < len(sorted_a) and sorted_a[i] <= sorted_b[j]:
      i+=1
    dict[sorted_b[j]] = i
  for x in b:
    print(dict[x], end=' ')


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))   
less_or_equal(a, b)