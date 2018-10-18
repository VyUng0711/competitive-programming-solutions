# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2957
class Triad():
  def __init__(self, source, target, weight):
    self.source = source
    self.target = target
    self.weight = weight
    
def findSet(u):
  if parents[u] != u:
    parents[u] = findSet(parents[u])
  return parents[u]


def unionSet(u, v):
  up = findSet(u)
  vp = findSet(v)
  if up == vp:
    return
  
  if ranks[up] > ranks[vp]:
    parents[vp] = up
  elif ranks[up] < ranks[vp]:
    parents[up] = vp
  else:
    parents[up] = vp
    ranks[vp] += 1
    
def kruskal():
  global result
  graph.sort(key=lambda edge: edge.weight)
  i = 0
  len_dist = 0
  while len_dist != n - 1 and i < len(graph):
    edge = graph[i]
    i += 1
    up = findSet(edge.source)
    vp = findSet(edge.target)
    if up != vp:
      unionSet(up, vp)
      len_dist += 1
#       dist.append(edge)
      result = max(result, edge.weight)
      
  if len_dist < n - 1:
    return False
  return True
    
    
while True:
  n, m = map(int, input().split())
  if n == 0 and m == 0:
    break
  graph = []
  parents = [i for i in range(n)]
  ranks = [0 for i in range(n)]
  result = 0
  for i in range(m):
    x, y, w = map(int, input().split())
    graph.append(Triad(x, y, w))
  connected = kruskal()
  if connected:
    print(result)
  else:
    print("IMPOSSIBLE")

