
# Alice in Amsterdam
# O(n^2 * m * t)  
INF = float('inf')
from collections import defaultdict

class Triad():
  def __init__(self, start, target, weight):
    self.start = start
    self.target = target
    self.weight = weight

    
def bellman_ford(start, dist, neg):
  dist[start] = 0
  for i in range(0, num_nodes):
    for j in range(num_edges):
      u = graph[j].start
      v = graph[j].target
      w = graph[j].weight
      if dist[u] != INF and dist[u] + w < dist[v]:
        if i == num_nodes - 1:
          neg[v] = True
        dist[v] = dist[u] + w


test_case = 1
while True:
  num_nodes = int(input())
  if num_nodes == 0:
    break
  num_edges = 0
  graph = []
  name_id = {}
  
  for i in range(num_nodes):
    this_node = list(input().split())
    node_name = this_node[0]
    name_id[i] = node_name
    targets = [int(x) for x in this_node[1:]]
    for j in range(len(targets)):
      if i == j:
        if targets[i] < 0:
          targets[i] = -INF
        else:
          targets[i] = 0
      if i == j or targets[j] != 0:
        graph.append(Triad(i, j, targets[j]))
        num_edges += 1
  num_queries = int(input())
  pairs = []
  queries = defaultdict(list)
  for q in range(num_queries):
    start, destination = list(map(int, input().split()))
    queries[start].append(destination)
    pairs.append((start, destination))
    
  print("Case #{}:".format(test_case))
  
  dist_results = [[INF] * num_nodes for x in range(num_nodes)]
  neg = [[False] * num_nodes for x in range(num_nodes)]
  for query in queries.keys():
    bellman_ford(query, dist_results[query], neg[query])
    for d in range(num_nodes):
      if neg[query][d] or dist_results[query][d] == -INF:
        dist_results[query][d] = None 


  for pair in pairs:
    dist = dist_results[pair[0]][pair[1]]
    if dist == None:
      print("NEGATIVE CYCLE")
    else:
      if dist == INF:
        dist = "NOT REACHABLE"
      start_city = name_id[pair[0]]
      dest_city = name_id[pair[1]]
      print("{}-{} {}".format(start_city, dest_city, dist))
  test_case += 1