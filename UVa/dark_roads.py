class Triad:
  def __init__(self, source, target, weight):
    self.source = source
    self.target = target
    self.weight = weight
  
  
def findSet(u):
  if u != parents[u]:
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
  global money_spent 
  graph.sort(key=lambda edge: edge.weight)
  i = 0
  while len(dist) != m - 1:
    edge = graph[i]
    i += 1
    u = findSet(edge.source)
    v = findSet(edge.target)
    if u != v:
      unionSet(u, v)
      dist.append(edge)
      money_spent += edge.weight
  
    
while True:
  m, n = map(int, input().split())
  if m == 0 and n == 0:
    break
  graph = []
  dist = []
  total_money = 0
  money_spent = 0
  parents = [i for i in range(m)]
  ranks = [0 for i in range(m)]
  for i in range(n):
    x, y, z = map(int, input().split())
    total_money += z
    graph.append(Triad(x, y, z))
  kruskal()
  print(total_money - money_spent)
    

