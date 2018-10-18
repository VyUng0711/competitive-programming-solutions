# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3649
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
    
def kruskal(num_cities):
  graph.sort(key = lambda edge: edge.weight)
  i = 0
  while len(dist) != num_cities - 1:
    edge = graph[i]
    i += 1
    u = findSet(edge.source)
    v = findSet(edge.target)
    if u != v:
      dist.append(edge)
      unionSet(u, v)
    
num_test = int(input())
for t in range(num_test):
  print("Case {}:".format(t + 1))
  
  num_cities = int(input())
  graph = []
  parents = {}
  ranks = {}
  dist = []
  # O(E*logV)
  for c in range(num_cities):
    parents[chr(65 + c)] = chr(65 + c)
    ranks[chr(65 + c)] = 0
    adjacents = list(map(int, input().split(', ')))
    for i in range(len(adjacents)):
      if adjacents[i] != 0:
        graph.append(Triad(chr(65 + c), chr(65 + i), adjacents[i])) 
  # print(ranks)
  # print(parents)
  kruskal(num_cities)
  for d in dist:
    print("{}-{} {}".format(d.source, d.target, d.weight))
    
