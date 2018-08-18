from collections import defaultdict
import queue
INF = float('inf')
# def floyd_warshall(graph):
def dijkstra(start, graph, dist):
    pq = queue.PriorityQueue()
    pq.put((start, 0))
    dist[start] = 0
    
    while not pq.empty():
        top = pq.get()
        for neighbor in graph[top[0]]:
            if top[1] + neighbor[1] < dist[neighbor[0]]:
                dist[neighbor[0]] = top[1] + neighbor[1]
                pq.put((neighbor[0], dist[neighbor[0]]))
              
while True:
  num_streets = int(input())
  if num_streets == 0:
    break
  graph_young = defaultdict(list)
  graph_old = defaultdict(list)
  
  my_dist = dict()
  prof_dist = dict()
  
  
  
  for s in range(num_streets):
    line = input().split()
    # print(line)
    if line[0] == "Y":
      if line[1] == "B":
        graph_young[line[3]].append((line[2], int(line[4])))
      graph_young[line[2]].append((line[3], int(line[4])))
      my_dist[line[2]] = INF
      my_dist[line[3]] = INF
    else:
      if line[1] == "B":
        graph_old[line[3]].append((line[2], int(line[4])))
        prof_dist[line[3]] = INF
      graph_old[line[2]].append((line[3], int(line[4])))
      prof_dist[line[2]] = INF
      prof_dist[line[3]] = INF
  my_start, prof_start = input().split()

  dijkstra(my_start, graph_young, my_dist)
  dijkstra(prof_start, graph_old, prof_dist)
#   print(my_dist)
#   print(prof_dist)
#   print(my_dist)
#   print(prof_dist)
  common_target = dict()
  min_dist = INF
  for k in my_dist.keys():
    if my_dist[k] != INF and k in prof_dist.keys() and prof_dist[k] != INF:
      common_target[k] = my_dist[k] + prof_dist[k]
      if my_dist[k] + prof_dist[k] < min_dist:
        min_dist = my_dist[k] + prof_dist[k]
  # print(common_target)
  # sorted_ct = [(k,v) for k,v in common_target.items()]
  if len(common_target) == 0:
    print("You will never meet.")
  else:
    min_targets = []
    for c, v in common_target.items():
      if v == min_dist:
        min_targets.append(c)
    print(min_dist, *sorted(min_targets))