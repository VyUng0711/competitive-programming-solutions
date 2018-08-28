# UVA
INF = float('inf')

def floyd_warshall():
  for k in range(num_towns):
    for i in range(num_towns):
      for j in range(num_towns):
        if dist[i][k] + dist[k][j] < dist[i][j]:
          dist[i][j] = dist[i][k] + dist[k][j]  
  
num_tests = int(input())
for t in range(num_tests):
  num_towns = int(input())
  graph = []
  dist = [[INF for i in range(num_towns)] for j in range(num_towns)]
  for o in range(num_towns):
    x, y = map(int, input().split())
    graph.append((x, y))
  for i in range(0, num_towns - 1):
    for j in range(i + 1, num_towns):
      cur_dist = ((graph[j][0] - graph[i][0])**2 + (graph[j][1] - graph[i][1])**2)**(0.5)
      if cur_dist <= 10.0:
        dist[i][j] = cur_dist
        dist[j][i] = cur_dist
  # print(dist)
  floyd_warshall()
  # print(dist)
  max_dist = -1
  for m in range(num_towns):
    for n in range(num_towns):
      if dist[m][n] != INF and dist[m][n] > max_dist:
        max_dist = dist[m][n]
  if t != 0:
    print()
  print("Case #{}:".format(t + 1))
  if max_dist == -1:
    print("Send Kurdy")
  else:
    print(max_dist)