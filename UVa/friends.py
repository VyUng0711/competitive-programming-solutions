#https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1549

  
def findSet(u):
  if parent[u] != u:
    parent[u] = findSet(parent[u])
  return parent[u]

def unionSet(u, v):
  up = findSet(u)
  vp = findSet(v)
  if up == vp:
    # print(set_size[vp])
    return
  if ranks[up] > ranks[vp]:
    parent[vp] = up
    set_size[up] += set_size[vp]
    # print(set_size[up])
  elif ranks[up] < ranks[vp]:
    parent[up] = vp
    set_size[vp] += set_size[up]
    # print(set_size[vp])
  else:
    parent[up] = vp
    ranks[vp] += 1
    set_size[vp] += set_size[up]
    # print(set_size[vp])

# Complexity: O(m * log (n))
num_test = int(input())
for t in range(num_test):
  
  n, m = map(int, input().split())
  parent = [i for i in range(n)]
  ranks = [0 for i in range(n)]
  set_size = [1 for i in range(n)]
  for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    unionSet(u, v)
    
  
#   for i in range(n):
#     set_size[findSet(i)] += 1
    
    
  print(max(set_size))
