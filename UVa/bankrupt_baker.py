# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2283
from collections import defaultdict
num_binders = int(input())
for b in range(num_binders):
  ingredient_to_cost = dict()
  title = input()
  print(title.upper())
  m, n, budget = map(int, input().split())
  for i in range(m):
    ingredient, cost = input().split()
    ingredient_to_cost[ingredient] = int(cost)
    requirement_to_cost = defaultdict(dict)
    affordable = dict()
  for j in range(n):
    name = input()
    k = int(input())
    total_cost = 0
    for l in range(k):
      requirement, x = input().split()
      requirement_to_cost[name][requirement] = int(x) * ingredient_to_cost[requirement]
      total_cost += requirement_to_cost[name][requirement]
    if total_cost <= budget:
      affordable[name] = total_cost
  sorted_aff = sorted(affordable.items(), key=lambda x: (x[1], x[0]))
  if len(sorted_aff) == 0:
    print('Too expensive!')
  else:
    for a in sorted_aff:
      print(a[0])
  print()
