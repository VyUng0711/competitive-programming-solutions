# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=382

def recurse(cur, indx):
  if len(cur) == 6:
    res.append(copy.deepcopy(cur))
    return 
  
  for i in range(indx, len(game)):
    cur.append(game[i])
    recurse(cur, i + 1)
    cur.pop()



first_test = True
while True:
  line = list(map(int, input().split()))
  if line[0] == 0:
    break

  if not first_test:
    print()
  first_test = False
  
  k = line[0]
  game = line[1:]
  res = []
  recurse([], 0)
  for r in res:
    print(*r)


