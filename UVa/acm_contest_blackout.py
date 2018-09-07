#https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1541import queue
import copy
import queue
INF = float('inf')
class Node:
  def __init__(self, id, dist):
    self.id = id
    self.dist = dist
  def __lt__(self, other):
    return self.dist <= other. dist

# O(m log n)
def prim(source, graph):
  dist = [INF for i in range(n)]
  path = [-1 for i in range(n)]
  visited = [False for i in range(n)]
  pq = queue.PriorityQueue()
  pq.put(Node(source, 0))
  dist[source] = 0
  while not pq.empty():
    top = pq.get()
    u = top.id
    visited[u] = True
    for neighbor in graph[u]:
      v = neighbor.id
      w = neighbor.dist
      if not visited[v] and w < dist[v]:
        dist[v] = w
        pq.put(Node(v, w))
        path[v] = u
  return sum(dist), path, dist
        
def printMST():
  ans = 0
  for i in range(n):
    if path[i] == -1:
      continue
    ans += dist[i]
    print("{0} - {1}: {2}".format(path[i], i, dist[i]))
  print("Weight: {}".format(ans))

num_test = int(input())
for t in range(num_test):
  n, m = map(int, input().split())
  graph = [[] for i in range(n)]

  edge_list = dict()
  for i in range(m):
    u, v, w = map(int, input().split())
    graph[u - 1].append(Node(v - 1, w))
    graph[v - 1].append(Node(u - 1, w))
    
    
#     edge_list[(u - 1, v - 1)] = w
#     edge_list[(v - 1, u - 1)] = w

        
  first, first_path, first_dist = prim(0, graph)
#   printMST()
  second = INF
  # print(first_path)
  # O(n m log n)
  for i in range(1, n):
    parent = first_path[i]
    # new_graph = copy.deepcopy(graph) # O(m)
#     for u_indx, u in enumerate(graph):
#       for node in u:
#         if i == u_indx and parent == node.id and node.dist == first_dist[i]:
#           node.dist = INF
#         if parent == u_indx and i == node.id and node.dist == first_dist[i]:
#           node.dist = INF
    
    for j in range(len(graph[i])):
      if parent == graph[i][j].id and graph[i][j].dist == first_dist[i]:
        graph[i][j].dist = INF
        break
    
    for j in range(len(graph[parent])):
      if i == graph[parent][j].id and graph[parent][j].dist == first_dist[i]:
        graph[parent][j].dist = INF
        break
    # print(parent)
#     removed_edge_weight = edge_list[(parent, i)]
#     edge_list[(parent, i)] = INF
#     edge_list[(i, parent)] = INF
    # print(edge_list)
#     new_graph = [[] for i in range(n)]
#     for k, v in edge_list.items():
#       new_graph[k[0]].append(Node(k[1], v))
#       new_graph[k[1]].append(Node(k[0], v))
    # print(start)
    temp, new_path, new_dist = prim(0, graph)
    # print(temp)
    if temp <= second:
      second = temp
      
#     for u_indx, u in enumerate(graph):
#       for node in u:
#         if i == u_indx and parent == node.id and node.dist == first_dist[i]:
#           node.dist = INF
#         if parent == u_indx and i == node.id and node.dist == first_dist[i]:
#           node.dist = INF
    
    for j in range(len(graph[i])):
      if parent == graph[i][j].id and graph[i][j].dist == INF:
        graph[i][j].dist = first_dist[i]
        break
    
    for j in range(len(graph[parent])):
      if i == graph[parent][j].id and graph[parent][j].dist == INF:
        graph[parent][j].dist = first_dist[i]
        break
#     edge_list[(parent, i)] = removed_edge_weight
#     edge_list[(i, parent)] = removed_edge_weight
    
  print(first, second)
