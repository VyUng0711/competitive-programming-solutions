# http://lightoj.com/volume_showproblem.php?problem=1041
import queue
INF = float('inf')
from collections import defaultdict
class Node:
  def __init__(self, name, dist):
    self.name = name
    self.dist = dist
  def __lt__(self, other):
    return self.dist <= other.dist
  
def prim(source):
  pq = queue.PriorityQueue()
  pq.put(Node(source, 0))
  dist[source] = 0
  while not pq.empty():
    top = pq.get()
    u = top.name
    visited[u] = True
    for neighbor in graph[u]:
      v = neighbor.name
      w = neighbor.dist
      if not visited[v] and w < dist[v]:
        dist[v] = w
        pq.put(Node(v, w))
        
num_test = int(input())
for t in range(num_test):
  blank = input()
  graph = defaultdict(list)  
  m = int(input())
  for i in range(m):
    u, v, w = input().split()
    graph[u].append(Node(v, int(w)))
    graph[v].append(Node(u, int(w)))
  start = u
  visited = {name: False for name in graph.keys()}
  dist = {name: INF for name in graph.keys()}

  prim(start)
  total = 0
  for d in dist.values():
    if d == INF:
      total = "Impossible"
      break
    total += d
  print("Case {}: {}".format(t + 1, total))
