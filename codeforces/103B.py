# http://codeforces.com/problemset/problem/103/B
def findSet(u):
  if parents[u] != u:
    parents[u] = findSet(parents[u])
  return parents[u]

def unionSet(u, v):
  up = findSet(u)
  vp = findSet(v)
  
  if up == vp:
    return True
  global count_p
  count_p -= 1
  if ranks[up] > ranks[vp]:
    parents[vp] = up
  elif ranks[up] < ranks[vp]:
    parents[up] = vp
  else:
    parents[up] = vp
    ranks[vp] += 1
  return False


n, m = map(int, input().split())
parents = [i for i in range(n)]
ranks = [0 for i in range(n)]

result = False

count_p = n # one set in the end
num_cycle = 0 # one and only one cycle (simple cycle)
for i in range(m):
  x, y = map(int, input().split())
  x -= 1
  y -= 1
  has_cycle = unionSet(x, y)
  if has_cycle:
    result = True
    num_cycle += 1


if count_p == 1 and result and num_cycle == 1:
  print("FHTAGN!")
else:
  print("NO")
    
    
  
  

