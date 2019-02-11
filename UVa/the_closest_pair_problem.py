# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1186

import math
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y


def distance(p1, p2):
  return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


# def merge(a1, a2):
#   res = []
#   i = 0
#   j = 0
#   k = 0
#   while i < len(a1) and j < len(a2):
#     if a1[i] <= a2[j]:
#       res.append(a1[i])
#       i += 1
#     else:
#       res.append(a2[j])
#       j += 1
#     k += 1
#   while i < len(a1):
#     res.append(a1[i])
#     i += 1
#     k += 1
#   while j < len(a2):
#     res.append(a2[j])
#     j += 1
#     k += 1
#   return res


def brute_force(point_set, left, right):
  # print(point_set)
  # print(left)
  # print(right)
  min_dist = float('inf')
  for i in range(left, right):
    for j in range(i + 1, right):
      min_dist = min(min_dist, distance(point_set[i], point_set[j]))
  return min_dist


def combine(point_set, left, right, mid, min_dist):
  mid_point = point_set[mid]
  targets = []
  for i in range(left, right):
    if abs(point_set[i].x - mid_point.x) <= min_dist:
      targets.append(point_set[i])
  
  # Sort by y coordinate:
  targets.sort(key = lambda p: p.y)
  global_min = min_dist
  for i in range(len(targets)):
    for j in range(i + 1, len(targets)):
      if targets[j].y - targets[i].y >= global_min:
        break
      global_min = min(global_min, distance(targets[i], targets[j]))
  return global_min



def divide_and_conquer(point_set, left, right):
  if right - left < 2:
    return float('inf')
  # if right - left <= 3:
  #   return brute_force(point_set, left, right)
  mid = (left + right) // 2
  min_left = divide_and_conquer(point_set, left, mid)
  # print(min_left)
  min_right = divide_and_conquer(point_set, mid, right)
  # print(min_right)
  min_dist = min(min_left, min_right)
  return combine(point_set, left, right, mid, min_dist)




while True:
  n = int(input())
  if n == 0:
    break
  all_points = []
  for i in range(n):
    x, y = map(float, input().split())
    all_points.append(Point(x, y))
    # Sort by x coordinate:
  all_points.sort(key=lambda p: p.x)

  res = divide_and_conquer(all_points, 0, n)
  if res < 10000:
    # print(res)
    print("{:.4f}".format(res))
  else:
    print("INFINITY")



