# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2498

def findSet(u):
  if parent[u] != u:
    parent[u] = findSet(parent[u])
  return parent[u]

def unionSet(u, v):
  up = findSet(u)
  vp = findSet(v)
  if up == vp:
    print(set_size[vp])
    return
  if ranks[up] > ranks[vp]:
    parent[vp] = up
    set_size[up] += set_size[vp]
    print(set_size[up])
  elif ranks[up] < ranks[vp]:
    parent[up] = vp
    set_size[vp] += set_size[up]
    print(set_size[vp])
  else:
    parent[up] = vp
    ranks[vp] += 1
    set_size[vp] += set_size[up]
    print(set_size[vp])


num_test = int(input())
for t in range(num_test):
  num_fs = int(input())
  parent = dict()
  set_size = dict()
  ranks = dict()
  pair = []
  for i in range(num_fs):
    u, v = input().split()
    parent[u] = u
    parent[v] = v
    ranks[u] = 0
    ranks[v] = 0
    set_size[u] = 1
    set_size[v] = 1
    pair.append((u, v))
  for a, b in pair:
    unionSet(a, b) 
