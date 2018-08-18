INF = float('inf')
class Triad():
  def __init__(self, start, target, weight):
    self.start = start
    self.target = target
    self.weight = weight
    
    
def bellman_ford(start):
  dist[start] = 0
  for i in range(n):
    for j in range(m):
      u = graph[j].start
      v = graph[j].target
      w = graph[j].weight
      if dist[u] != INF and dist[u] + w < dist[v]:
        if i == n - 1:
          dist[v] = -INF
        else:
          dist[v] = dist[u] + w
  return False

while True:
  n, m, q, s = map(int, input().split())
  if n == 0 and m == 0 and q == 0 and s == 0:
    break
  graph = []
  dist = [INF] * n
  for i in range(m):
    u, v, w = map(int, input().split())
    graph.append(Triad(u, v, w))
  bellman_ford(s)
  for _ in range(q):
    j = int(input())
    if dist[j] == -INF:
      print("-Infinity")
    elif dist[j] == INF:
      print("Impossible")
    else:
      print(dist[j]) 
  print()