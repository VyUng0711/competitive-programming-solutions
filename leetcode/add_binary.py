# https://leetcode.com/problems/add-binary/description/
# Method 1: without using Python built-in library
def add_binary(a, b):
  max_len = max(len(a), len(b))
  if len(a) < max_len:
    a = "0" * (max_len - len(a)) + a
  if len(b) < max_len:
    b = "0" * (max_len - len(b)) + b
  result = []
  remainder = 0
  for i in range(max_len - 1, -1, -1):
    this_sum = int(a[i]) + int(b[i]) + remainder
    if this_sum == 3:
      result.append('1')
      if i == 0:
        result.append('1')
      else:
        remainder = 1
    elif this_sum == 2:
      result.append('0')
      if i == 0:
        result.append('1')
      else:
        remainder = 1
    elif this_sum <= 1:
      result.append(str(this_sum))
      remainder = 0
  result.reverse()
  return "".join(result)

# Method 2:
def add_binary(a, b):
  return bin(int(a, 2) + int(b, 2))[2:]

