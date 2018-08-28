# UVA
import queue
INF = float('inf')
class Triad():
  def __init__(self, start, target, weight):
    self.start = start
    self.target = target
    self.weight = weight
    
    
def bfs(start):
  q = queue.Queue()
  visited = [False] * num_rooms
  visited[start] = True
  q.put(start)
  while q.empty() == False:
    u = q.get()
    for v in adjacent[u]:
      if v == num_rooms - 1:
        return True
      if visited[v] == False:
        visited[v] = True
        q.put(v)
  return False

def bellman_ford(start):
  dist[start] = 100
  for i in range(0, num_rooms - 1):
    for u in range(num_rooms):
      for v in adjacent[u]:
        w = room_energy[v]
        if dist[u] <= 0:
          break
        if dist[u] != -INF and dist[u] + w > dist[v]:
          dist[v] = dist[u] + w


while True:
  num_rooms = int(input())
  if num_rooms == -1:
    break
  graph = []
  room_energy = {}
  doorways = []
  graph = []
  adjacent = [[] for i in range(num_rooms)]
  
  for i in range(num_rooms):
    cur = list(map(int, input().split()))
    room_energy[i] = cur[0]
    num_edges = cur[1]
    dest_rooms = cur[2:]
    for dest_room in dest_rooms:
#       doorways.append((i, dest_room - 1))
      adjacent[i].append(dest_room - 1)
#   for doorway in doorways:
#     adjacent[doorway[0]].append(doorway[1]
#     graph.append(Triad(doorway[0], doorway[1], -room_energy[doorway[1]]))
#   print(adjacent)
  dist = [-INF] * num_rooms
  res = bellman_ford(0)
#   print(dist)
  if dist[num_rooms - 1] > 0: # -INF
    print("winnable")
  else:
#     if res:
#       node_in_cycle = res[1]
#       visited = [False] * num_rooms
#       target_visited = bfs(node_in_cycle)
#       print(target_visited)
#       if target_visited:
#         print("winnable")
#       else:
#         print("hopeless")
#     else:
#       print("hopeless")
    res = False
    for u in range(num_rooms):
      for v in adjacent[u]:
        w = room_energy[v]
        if dist[u] > 0 and dist[u] != -INF and dist[v] < dist[u] + w and bfs(u):
          res = True
    if res:
      print('winnable')
    else:
      print('hopeless')  
      
      
# 6
# 0 1 2
# -99 1 3
# 1 1 4
# 1 1 5
# 1 2 3 6
# -100 0
