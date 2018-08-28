# https://codeforces.com/problemset/problem/295/B
INF = float('inf')
import copy

def floyd_warshall():
  for k in range(num_v):
    for i in range(num_v):
      for j in range(num_v):
        if dist[i][k] + dist[k][j] < dist[i][j]:
          dist[i][j] = dist[i][k] + dist[k][j]
          
    for i in range(k + 1):
      for j in range(k + 1):
        result[num_v - k - 1] += dist[i][j]
          
num_v = int(input())

graph = [[INF for i in range(num_v)] for j in range(num_v)]

for i in range(num_v):
  this_line = list(map(int, input().split()))
  for j in range(len(this_line)):
    graph[i][j] = this_line[j]
    
dist = copy.deepcopy(graph)

delete_vts = list(map(int, input().split()))
delete_vts = [x - 1 for x in delete_vts]

result = [0 for _ in range(num_v)]
delete_order = dict()
for i in range(num_v):
  delete_order[delete_vts[i]] = num_v - 1 - i

for i in range(num_v):
  for j in range(num_v):
    dist[delete_order[i]][delete_order[j]] = graph[i][j]

floyd_warshall()
print(*result) 
    