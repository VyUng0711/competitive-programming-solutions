# https://www.spoj.com/problems/MICEMAZE/
import math
import queue
INF = math.inf
class Node:
  def __init__(self, id, dist):
    self.id = id
    self.dist = dist
  def __lt__(self, other):
    return self.dist < other.dist
def dijkstra(s, d):
  dist = [INF for x in range(n)]
  pq = queue.PriorityQueue()
  pq.put(Node(s, 0))
  dist[s] = 0
  while not pq.empty():
    u = pq.get()
    if u.id == d:
      return dist[u.id]
    for v in graph[u.id]:
      if dist[v.id] > v.dist + u.dist:
        dist[v.id] = v.dist + u.dist
        pq.put(Node(v.id, dist[v.id]))
n = int(input())
graph = [[] for x in range(n)]
e = int(input())
t = int(input())
m = int(input())
for i in range(m):
  u, v, dist = map(int, input().split())
  graph[u - 1].append(Node(v-1, dist))
count = 0
for mice in range(n):
  this_time = dijkstra(mice, e)
  if this_time <= t:
    count+=1
print (count)

        
  