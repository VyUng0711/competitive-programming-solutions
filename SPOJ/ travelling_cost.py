# https://www.spoj.com/problems/TRVCOST/
import queue
import math
INF = math.inf
class Node:
  def __init__(self, id, dist):
    self.id = id
    self.dist = dist
  def __lt__(self, other):
    return self.dist <= other.dist
  
n = int(input())
graph = [[] for i in range(501)]
dist = [INF for i in range(501)]
path = [-1 for i in range(501)]
for i in range(n):
  u, v, w = map(int, input().split())
  graph[u].append(Node(v, w))
  graph[v].append(Node(u, w))
u = int(input())
q = int(input())
queries = []
for _ in range(q):
  queries.append(int(input()))

def dijkstra (s):
  q = queue.PriorityQueue()
  q.put(Node(s, 0))
  dist[s] = 0
  while not q.empty():
    cur = q.get()
    for neighbor in graph[cur.id]:
      if dist[neighbor.id] > cur.dist + neighbor.dist:
        dist[neighbor.id] = cur.dist + neighbor.dist
        path[neighbor.id] = cur.id
        q.put(Node(neighbor.id, dist[neighbor.id]))
        
        
dijkstra(u)

for j in queries:
  if dist[j] == INF:
    print ("NO PATH")
  else:
    print (dist[j])