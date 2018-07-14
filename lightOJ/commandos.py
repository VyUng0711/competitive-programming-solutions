import queue
INF = 10 ** 9
class Node:
  def __init__(self, id, dist):
    self.id = id
    self.dist = dist
  def __lt__(self, other):
    return self.dist < other.dist

def dijkstra(s, dist, d = None):
  pq = queue.PriorityQueue()
  pq.put(Node(s, 0))
  dist[s] = 0
  while not pq.empty():
    u = pq.get()
    if d and d == u.id:
      break
    for v in graph[u.id]:
      if dist[v.id] > v.dist + u.dist:
        dist[v.id] = v.dist + u.dist
        pq.put(Node(v.id, dist[v.id]))

    
num_tests= int(input())
for t in range(num_tests):
  num_buildings = int(input())
  num_roads = int(input())
  graph = [[] for x in range(num_buildings)]
  for r in range(num_roads):
    u, v = map(int, input().split())
    graph[u].append(Node(v, 1))
    graph[v].append(Node(u, 1))
  s, d = map(int, input().split())
  
  # Distances from source to all the buildings:
  dist_from_source = [INF for x in range(num_buildings)]

  # Find shortest path from source to all the buildings
  dijkstra(s, dist_from_source)
  
  # Find shortest path from destination to all the buildings 
  dist_to_destination = [INF for x in range(num_buildings)]
  # Find the shortest path from all the farthest buildings to destination
  dijkstra(d, dist_to_destination)
  
  result = max(dist_from_source[x] + dist_to_destination[x] for x in range(num_buildings))
  
  
  print("Case {}: {}".format(t+1, result))