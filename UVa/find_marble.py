import bisect
def bs_first(a, left, right, x):
  while left <= right:
    mid = (left + right) // 2
    if a[mid] == x and (x > a[mid - 1] or mid == left):
      return mid
    elif a[mid] < x:
      left = mid + 1
    else:
      right = mid - 1
  return -1

test_number = 1
while True:
  n, q = map(int, input().split())
  if n == 0 and q == 0:
    break
  marbles = []
  for i in range(n):
    marbles.append(int(input()))
  
  sorted_m = sorted(marbles)
  
  queries = []
  for j in range(q):
    queries.append(int(input()))
    
  print("CASE# {}:".format(test_number))
  for q in queries:
    # index = bs_first(sorted_m, 0, len(sorted_m) - 1, q)
    index = bisect.bisect_left(sorted_m, q, 0, len(sorted_m))
    # if index != -1:
    if index < len(sorted_m) and sorted_m[index] == q:
      print("{} found at {}".format(q, index + 1))
    else:
      print("{} not found".format(q))
      
  test_number += 1