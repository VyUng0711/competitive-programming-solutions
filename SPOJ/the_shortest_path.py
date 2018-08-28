# https://www.spoj.com/problems/SHPATH/
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
  pq = queue.PriorityQueue()
  pq.put(Node(s, 0))
  dist[s] = 0
  while not pq.empty():
    u = pq.get()
    if u.id == d:
      break
    for v in graph[u.id]:
      if dist[v.id] > v.dist + u.dist:
        dist[v.id] = v.dist + u.dist
        path[v.id] = u.id
        pq.put(Node(v.id, dist[v.id]))
  #return dist[d]

  
s = int(input())
n = int(input())
graph = [[] for x in range(n)]
cities = {}
for i in range(n):
  city_name = input()
  cities[city_name] = i
  p = int(input())
  for j in range(p):
    neighbor, distance = map(int, input().split())
    neighbor_id = neighbor - 1
    graph[i].append(Node(neighbor_id, distance))

r = int(input())
for _ in range(r):
  s, d = input().split()
  s_id = cities[s]
  d_id = cities[d]
  dist = [INF for x in range(n)]
  path = [-1 for x in range(n)]
  dijkstra(s_id, d_id)
  print (dist[d_id])
  

        
      
  
  
  