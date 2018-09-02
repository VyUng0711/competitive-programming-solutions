# UVA
INF = 10 ** 9
class Triad:
  def __init__(self, s, t, w):
    self.s = s
    self.t = t
    self.w = w
    
def bellman_ford(source):
  dist[source] = 0
  for i in range(num_v):
    for j in range(num_e):
      u, v, w = graph[j].s, graph[j].t, graph[j].w
      if dist[u] != INF and dist[u] + w < dist[v]:
        if i == num_v - 1:
          return True
        dist[v] = dist[u] + w
  return False
      
      
num_cases = int(input())
for ci in range(num_cases):
  num_v, num_e = map(int, input().split())
  graph = []
  dist = [INF] * num_v
  for ei in range(num_e):
    x, y, t = map(int, input().split())
    graph.append(Triad(x, y, t))
  result = bellman_ford(0)
  if result:
    print("possible")
  else:
    print("not possible")
  
  
    
  
