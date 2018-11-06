import queue
import copy 
import heapq

class Triad():
  def __init__(self, source, target, weight):
    self.source = source
    self.target = target
    self.weight = weight
    
  def __lt__(self, other):
    return self.weight < other.weight

  
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
  this_graph = copy.deepcopy(graph)
  result = 0
  len_dist = 0
  while len_dist != n - 1 and len(this_graph) > 0:
    edge = heapq.heappop(this_graph)
    up = findSet(edge.source)
    vp = findSet(edge.target)
    if up != vp:
      unionSet(up, vp)
      result += edge.weight
      len_dist += 1
      
  if len_dist < n - 1:
    print(-1)
  else:
    print(result)

num_test = int(input())
for t in range(num_test):
  print("Case {}:".format(t + 1))
  
  n, w = map(int, input().split())
  graph = []
  
  # Complexity: w * O(E log V)
  for i in range(w):
    parents = [i for i in range(n)] # O(N)
    ranks = [0 for i in range(n)] # O(N)
    x, y, w = map(int, input().split())
    
    # insertion sort
    x -= 1
    y -= 1
    heapq.heappush(graph, Triad(x, y, w)) # O(log(E))

    kruskal() # O(E log V)
