import copy
INF = float('inf')

def floyd_warshall():
  for k in range(m):
    for i in range(m):
      for j in range(m):
        if dist[i][k] == 1 and dist[k][j] == 1 and dist[i][j] == INF:
          dist[i][j] = 2

num_test = int(input())
for t in range(num_test):
  first_line = list(input())
  m = len(first_line)
  graph = [[None for i in range(m)] for j in range(m)]

  for j in range(m):
    graph[0][j] = INF if first_line[j] == "N" else 1
  for i in range(1, m):
    line = list(input())
    for j in range(m):
      graph[i][j] = INF if line[j] == "N" else 1
      
  dist = copy.deepcopy(graph)
  floyd_warshall()

  max_key = None
  max_value = -1
  for x in range(m):
    num_possible = 0
    for y in range(m):
      if dist[y][x] == 2 and y != x:
        num_possible += 1
    if num_possible > max_value: 
      max_value = num_possible
      max_key = x 
  print(max_key, max_value)
       
      
    
  
    
