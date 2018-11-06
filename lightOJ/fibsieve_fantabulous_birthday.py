import math
num_tests = int(input())
for t in range(num_tests):
  s = int(input())
  root = math.ceil(math.sqrt(s))
  remain = root ** 2 - s
  if remain < root:
    if root % 2 == 0:
      x = root
      y = remain + 1
    else:
      y = root
      x = remain + 1
  else:
    if root % 2 == 0:
      x = s - (root - 1)**2
      y = root
    else:
      x = root
      y = s - (root - 1)**2

  print("Case {}: {} {}".format(t + 1, x, y))


