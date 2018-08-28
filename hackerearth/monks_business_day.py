# https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/monks-business-day/
INF = float('inf')
class Triad():
  def __init__(self, source, target, weight):
    self.source = source
    self.target = target
    self.weight = weight
    
def bellman_ford(start):
  dist[start] = 0
  for i in range(num_items):
    for j in range(num_dealers):
      u = graph[j].source
      v = graph[j].target
      w = graph[j].weight
      if dist[u] != -INF and dist[u] + w > dist[v]:
        if i == num_items - 1:
          return True
        dist[v] = dist[u] + w
  return False

num_tests = int(input())
for t in range(num_tests):
  num_items, num_dealers = map(int, input().split())
  graph = []
  dist = [-INF] * num_items
  for d in range(num_dealers):
    i, j, C = map(int, input().split())
    i -= 1
    j -= 1
    graph.append(Triad(i, j, C))
  result = bellman_ford(0)
  if result: 
    print("Yes")
  else:
    print("No")

    
