def binary_search(a, left, right, x):
  while left <= right:
    mid = (left + right)//2
    if a[mid] == x:
      return mid
    elif a[mid] < x:
      left = mid + 1
    else:
      right = mid - 1
  return -1

num_test = int(input())
for t in range(num_test):
  num_friends, price = map(int, input().split())
  money = list(map(int, input().split()))
  money.sort()
  num_pairs = 0
  for m in range(len(money)):
    found = binary_search(money, m+1, len(money) - 1, price - money[m])
    if found != -1:
      num_pairs += 1
  print(num_pairs)