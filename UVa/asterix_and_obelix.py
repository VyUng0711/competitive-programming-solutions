INF = float('inf')
import copy

def floyd_warshall():
  for t in range(3):
    for k in range(num_cities):
      for i in range(num_cities):
        for j in range(num_cities):
          temp_highest_feast_cost = max(highest_feast_costs[i][k], highest_feast_costs[k][j])
          if dist[i][j] + highest_feast_costs[i][j] > dist[i][k] + dist[k][j] + temp_highest_feast_cost:
            dist[i][j] = dist[i][k] + dist[k][j]
            highest_feast_costs[i][j] = temp_highest_feast_cost

case_id = 1
while True:
  num_cities, num_roads, num_queries = map(int, input().split())
  if num_cities == num_roads == num_queries == 0:
    break
  
  highest_feast_costs = [[INF for i in range(num_cities)] for j in range(num_cities)]
  feast_costs = list(map(int, input().split()))
  for f in range(num_cities):
    highest_feast_costs[f][f] = feast_costs[f]
    
  graph = [[INF for i in range(num_cities)] for j in range(num_cities)]
  
  for r in range(num_roads):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = w
    graph[v][u] = w
    higher_feast_cost = max(highest_feast_costs[u][u], highest_feast_costs[v][v])
    highest_feast_costs[u][v] = higher_feast_cost
    highest_feast_costs[v][u] = higher_feast_cost
    
  # print(highest_feast_costs)
  dist = copy.deepcopy(graph)
  floyd_warshall()
  
  print("Case #{}".format(case_id))
  
  for q in range(num_queries):
    s, d = map(int, input().split())
    s -= 1
    d -= 1
    if dist[s][d] == INF:
      print("-1")
    else:
      print(dist[s][d] + highest_feast_costs[s][d])
    

  case_id += 1