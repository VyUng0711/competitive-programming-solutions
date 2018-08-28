# UVA
import math
def get_result(x):
  return (p * math.e ** (-x) + q * math.sin(x) + r * math.cos(x) + s * (math.tan(x)) + t * x ** 2 + u)
# 0 <= p, r <= 20 => (p * e ^ -x + r * cos(x)) increasing with x
# -20 <= q, s, t <= 0 => (q * sin(x) + s * tan(x) + t) increasing with x

def binary_search(left, right):
  for i in range(100):
    mid = (left + right) / 2
    res = get_result(mid)
    # print(mid)
    if abs(res) < 0.000000001:
      return mid
    elif res > 0:
      left = mid
    else:
      right = mid
  return False

while True:
  try:
    p, q, r, s, t, u = map(int, input().split())
  except EOFError:
    break
  result = binary_search(0, 1)
  if result:
    # print(round(result, 4))
    print('{:.4f}'.format(result))
  else:
    print("No solution")