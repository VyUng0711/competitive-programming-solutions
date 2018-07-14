import queue
INF = 10 ** 9

class Node():
  def __init__(self, id, dist):
    self.id = id
    self.dist = dist
  def __lt__(self, other):
    return (self.dist < other.dist)
  
def dijkstra(s, dist, graph):
  pq = queue.PriorityQueue()
  pq.put(Node(s, 0))
  dist[s] = 0
  while not pq.empty():
    u = pq.get()
    for v in graph[u.id]:
      if dist[v.id] > v.dist + u.dist:
        dist[v.id] = v.dist + u.dist
        pq.put(Node(v.id, dist[v.id]))
  

num_sets = int(input())
for _ in range(num_sets):
  n, m, k, s, t = map(int, input().split())
  s -= 1
  t -= 1 
  graph = [[] for x in range(n)]
  inverse_graph = [[] for x in range(n)]

  for i in range(m):
    di, ci, li = map(int, input().split())
    di -= 1
    ci -= 1
    graph[di].append(Node(ci, li))
    inverse_graph[ci].append(Node(di, li))

  dist_from_source = [INF for x in range(n)]
  dist_from_destination = [INF for x in range(n)]
  dijkstra(s, dist_from_source, graph)
  dijkstra(t, dist_from_destination, inverse_graph)
  candidates = []
  candidates.append(dist_from_source[t])

  for j in range(k):
    uj, vj, qj = map(int, input().split())
    uj -= 1
    vj -= 1
    candidates.append(dist_from_source[uj] + qj + dist_from_destination[vj])
    candidates.append(dist_from_source[vj] + qj + dist_from_destination[uj])
    
  if min(candidates) == INF:
    print(-1)
  else:
    print(min(candidates))