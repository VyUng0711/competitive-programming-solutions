# UVA
import copy
INF = float('inf')


def floyd_warshall():
    for k in range(20):
        for i in range(20):
            for j in range(20):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]            
test_id = 1
while True:
    graph = [[INF for i in range(20)] for j in range(20)]
    for li in range(19):
        try:
          this_line = input()
        except EOFError:
          break
        this_line = list(map(int, this_line.split()))
        for v in this_line[1:]:
            graph[li][v - 1] = 1
            graph[v-1][li] = 1
        
    if li == 0:
      break
        
    # print(graph)
    dist = copy.deepcopy(graph)
    floyd_warshall()
    # print(dist)
    n = int(input())
    queries = []
    for _ in range(n):
      s, d = map(int, input().split())
      queries.append((s, d))
    print("Test Set #{}".format(test_id))
    
    for q in queries:
      print("{} to {}: {}".format(q[0], q[1], dist[q[0] - 1][q[1] - 1]))
    
    test_id += 1
      
    
    
