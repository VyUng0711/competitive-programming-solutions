# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2833
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
  global cost_roads, num_airports
  
  graph.sort(key=lambda edge: edge.weight)
  i = 0
  cost_roads = num_loc * cost_a
  num_airports = num_loc
  num_connections = 0
  while num_connections != num_loc - 1 and i < len(graph) and graph[i].weight < cost_a:
    edge = graph[i]
    i += 1
    up = findSet(edge.source)
    vp = findSet(edge.target)
    if up != vp:
      unionSet(up, vp)
      num_airports -= 1
      cost_roads -= cost_a
      num_connections += 1
      cost_roads += edge.weight
      
    
num_test = int(input())

for t in range(num_test):
  num_loc, num_roads, cost_a = map(int, input().split())
  parents = [i for i in range(num_loc)]
  ranks = [0 for i in range(num_loc)]
  graph = []

  for i in range(num_roads):
    x, y, c = map(int, input().split())
    x -= 1
    y -= 1
    graph.append(Triad(x, y, c))
    
  num_airports = 0
  cost_roads = 0

  kruskal()
  print("Case #{}: {} {}".format(t + 1, cost_roads, num_airports))
  
  
    
    
