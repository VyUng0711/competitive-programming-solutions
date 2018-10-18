# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=16&page=show_problem&problem=2757
class Triad:
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
  while len(dist) != s - 1 and i < len(graph):
    edge = graph[i]
    i += 1
    up = findSet(edge.source)
    vp = findSet(edge.target)
    if up != vp:
      unionSet(up, vp)
      dist.append(edge)
      result += edge.weight
      
  if i == len(graph) and len(dist) < s - 1:
    return False
  return True
    
    
while True:
  s, c = map(int, input().split())
  if s == 0 and c == 0:
    break
    
    
  parents = {}
  ranks = {}
  graph = []
  dist = []
  result = 0
  for i in range(s):
    s_name = input()
    parents[s_name] = s_name
    ranks[s_name] = s_name
    
  for j in range(c):
    u, v, w = input().split()
    graph.append(Triad(u, v, int(w)))
    
  
  start = input()
  has_mst = kruskal()
  if has_mst:
    print(result)
  else:
    print("Impossible")

