# Method 1: binary search
def my_sqrt(x):
  left = 0
  right = x
  if x == 1 or x == 0:
    return x
  while right - left >= 0:
    mid = (left + right) / 2
    if abs(mid ** 2 - x) < 0.00001:
      return int(mid)
    else:
      if mid ** 2 > x:
        right = mid
      elif mid ** 2 < x:
        left = mid

# Method 2: binary search
def my_sqrt(x):
  if x == 0:
    return 0
  left = 0
  right = x
  while left <= right:
    mid = (left + right) // 2
    if mid ** 2 == x:
      return mid
    elif mid ** 2 < x:
      left = mid + 1
    else:
      right = mid - 1
  return left - 1

# Method 3: Newton Method

