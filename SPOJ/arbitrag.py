# https://www.spoj.com/problems/ARBITRAG/
import copy
import sys
def floyd_warshall():
  for k in range(num_cur):
    for i in range(num_cur):
      for j in range(num_cur):
        if dist[i][k] * dist[k][j] > dist[i][j]:
          dist[i][j] = dist[i][k] * dist[k][j]
          
case_number = 1
while True:
  num_cur = int(input())
  if num_cur == 0:
    break
  map_cur = dict()
  graph = [[0 for i in range(num_cur)] for j in range(num_cur)]
  for cur_index in range(num_cur):
    map_cur[input()] = cur_index
    graph[cur_index][cur_index] = 1
    
  num_exchange = int(input())
  for e in range(num_exchange):
    cur_e = input().split()
    start = cur_e[0]
    graph[map_cur[cur_e[0]]][map_cur[cur_e[2]]] = float(cur_e[1])
  # print(graph)
  dist = copy.deepcopy(graph)
  floyd_warshall()
  print(dist, sys.stderr)
  result = False
  for i in range(num_cur):
    if dist[i][i] > 1:
      result = True
      break
  if result:
    print("Case {}: Yes".format(case_number))
  else:
    print("Case {}: No".format(case_number))
  end = input()
  case_number += 1