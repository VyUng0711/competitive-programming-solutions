import queue
INF = 10**9

class Node:
  def __init__(self, id, dist):
    self.id = id
    self.dist = dist
  def __lt__(self, other):
    return self.dist < other.dist
  
num_cities, num_roads, num_choco_cities, expiry_time = map(int, input().split())
choco_cities = list(map(int, input().split()))
graph = [[] for x in range(num_cities)]
for _ in range(num_roads):
  u, v, d = map(int, input().split())
  graph[u-1].append(Node(v-1, d))
  graph[v-1].append(Node(u-1, d))

friend, you = map(int, input().split())

def dijkstra(s, dist, d = None):
  pq = queue.PriorityQueue()
  pq.put(Node(s, 0))
  dist[s] = 0
  while not pq.empty():
    u = pq.get()
    if d != None and u.id == d:
      break
    for v in graph[u.id]:
      if dist[v.id] > v.dist + u.dist:
        dist[v.id] = v.dist + u.dist
        pq.put(Node(v.id, dist[v.id]))
  
  
def find_min_distance():
  # Find distances from friend to chocolates:
  dist_to_chocolates = [INF for x in range(num_cities)]
  dijkstra(friend - 1, dist_to_chocolates)
  reached_chocolates = {}
  for c in choco_cities:
    if dist_to_chocolates[c - 1] != INF:
      reached_chocolates[c - 1] = dist_to_chocolates[c - 1]
  if not reached_chocolates:
    return -1
  # Find distances from chocolates to you:
  all_dists = []
  dist_from_chocolates = [INF for x in range(num_cities)]
  dijkstra(you - 1, dist_from_chocolates)
  
  for key, value in reached_chocolates.items():
    if dist_from_chocolates[key] <= expiry_time: 
        all_dists.append(value + dist_from_chocolates[key])
  if len(all_dists) == 0:
    return -1
  else:
    return min(all_dists)
  
print(find_min_distance())