# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=670  

import sys
sys.setrecursionlimit(1000000)
def get_all_str(cur, count):
  if count > h:
    return

  if len(cur) == n:
    if count == h:
      print(''.join(cur))
    return

  else:
    for i in range(2):
      cur.append(str(i))
      if i == 1:
        get_all_str(cur, count + 1)
      else:
        get_all_str(cur, count)
      cur.pop()



num_d = int(input())
for d in range(num_d):
  input()
  n, h = map(int, input().split())
  get_all_str([], 0)
  if d != num_d - 1:
    print()


