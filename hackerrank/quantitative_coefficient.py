class Triad:
  def __init__(self, source, target, weight):
    self.source = source
    self.target = target
    self.weight = weight


def findSet(u):
  if parent[u] != u:
    parent[u] = findSet(parent[u])
  return parent[u]

def unionSet(u, v):
  up = findSet(u)
  vp = findSet(v)
  if up == vp:
    return
  if ranks[up] > ranks[vp]:
    parent[vp] = up
  elif ranks[up] < ranks[vp]:
    parent[up] = vp
  else:
    parent[up] = vp
    ranks[vp] += 1

# O(mlogm + mlogn) = O(mlog(m*n))
def kruskal():
  # O(mlogm)
  graph.sort(key= lambda edge: edge.weight)
  i = 0
  res = 1
  while len(dist) != n - 1: # O(m)
    edge = graph[i]
    i += 1
    u = findSet(edge.source) # O(logn)
    v = findSet(edge.target) # O(logn)
    if u != v:
      dist.append(edge)
      res *= edge.weight
      unionSet(u, v) # O(1)
  return res % (10 ** 9 + 7)


num_test = int(input())
for t in range(num_test):
  n, m = map(int, input().split())
  graph = []
  dist = []
  parent = [i for i in range(m)]
  ranks = [0 for i in range(m)]
  for i in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph.append(Triad(u, v, w))

  print(kruskal())


