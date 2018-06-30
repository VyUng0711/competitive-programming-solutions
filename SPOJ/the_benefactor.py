def find_longest_path_from_node(graph, source):
  stack = []
  stack.append(source)
  distances = [0]*n
  distances[source] = 0
  max_distance = 0
  max_index = source
  while len(stack) != 0:  
    u = stack.pop()
    for node in graph[u]:
      if distances[node] == 0: 
        stack.append(node)
        distances[node] = distances[u] + edges[(u, node)]
        if distances[node] > max_distance:
          max_distance = distances[node]
          max_index = node         
  return (max_distance, max_index)

num_test_case= int(input())
for t in range(num_test_case):
  n = int(input())
  
  graph = [[]*x for x in range(n)]
  edges = {}
  for i in range(n-1):
    u, v, edge = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
    edges[(u-1, v-1)] = edge
    edges[(v-1, u-1)] = edge
  random_longest_distance_index = find_longest_path_from_node(graph, 0)[1]
  longest_distance = find_longest_path_from_node(graph, random_longest_distance_index)[0]
  print (longest_distance)
  
  