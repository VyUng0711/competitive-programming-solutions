# http://codeforces.com/problemset/problem/424/B
import math
n, s = map(int, input().split())
map_dist_pop = dict()
for i in range(n):
  x, y, p = map(int, input().split())
  dist = math.sqrt(x ** 2 + y ** 2)
  map_dist_pop[dist] = map_dist_pop.get(dist, 0) + p
# print(map_dist_pop)
sorted_map = sorted(map_dist_pop.items())
# sorted_map = [(k, v) for k, v in sorted(map_dist_pop.items())]

sum_pop = s
res = -1
for loc in sorted_map:
  sum_pop += loc[1]
  if sum_pop >= 10**6:
    res = loc[0]
    break
print(res)
