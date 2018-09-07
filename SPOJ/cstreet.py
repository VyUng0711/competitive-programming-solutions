reimport queue
INF = float('inf')
# https://www.spoj.com/problems/CSTREET/
class Node:
  def __init__(self, id, dist):
    self.id = id
    self.dist = dist
  def __lt__(self, other):
    return self.dist <= other.dist
  
def prim(source):
  pq = queue.PriorityQueue()
  pq.put(Node(source, 0))
  dist[source] = 0
  while not pq.empty():
    top = pq.get()
    u = top.id
    visited[u] = True
    for neighbor in graph[u]:
      v = neighbor.id
      w = neighbor.dist
      if not visited[v] and w < dist[v]:
        dist[v] = w
        path[v] = u
        pq.put(Node(v, w))
        
  
num_test = int(input())
for t in range(num_test):
  p = int(input())
  n = int(input())
  m = int(input())
  graph = [[] for i in range(n)]
  dist = [INF for i in range(n)]
  visited = [False for i in range(n)]
  path = [-1 for i in range(n)]
  for i in range(m):
    u, v, w = map(int, input().split())
    graph[u - 1].append(Node(v - 1, w * p))
    graph[v - 1].append(Node(u - 1, w * p))
prim(0)
print(sum(dist))
