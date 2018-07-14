import queue
INF = 10 ** 9

class Node():
  def __init__(self, id, dist):
    self.id = id
    self.dist = dist
  def __lt__(self, other):
    return (self.dist < other.dist)
  
def dijkstra(s):
  pq = queue.PriorityQueue()
  
  pq.put(Node(s, 0))
  dist[s] = 0
  while not pq.empty():
    u = pq.get()
    for v in graph[u.id]:
      this_dist = max(v.dist, u.dist)
      if dist[v.id] > this_dist:
        dist[v.id] = this_dist
        pq.put(Node(v.id, dist[v.id]))
      
num_test = int(input())    
for ti in range(num_test):
  blank_line = input()
  n, m = map(int, input().split())
  graph = [[] for x in range(n)]
  for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append(Node(v, w))
    graph[v].append(Node(u, w))
  t = int(input())
  dist = [INF for x in range(n)]
  dijkstra(t)
  print("Case: {}".format(ti + 1))
  for d in dist:
    if d == INF:
      print("Impossible")
    else:
      print(d)
  