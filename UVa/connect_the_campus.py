# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1338
import math
import queue
INF = float('inf')
class Scanner:
    def __generator__():
        while True:
            try:
                buff = input().strip().split()
                for x in buff:
                    yield x
            except EOFError:
                exit()
                
    sc = __generator__()
    def next():
        return Scanner.sc.__next__()
      
# class Node:
#     def __init__(self, id, dist):
#         self.id = id
#         self.dist = dist
#     def __lt__(self, other):
#         return(self.dist <= other.dist)
     
def prim(source, graph, dist, visited):
    n = len(graph)
    pq = queue.PriorityQueue()
    pq.put((0, source))
    dist[source] = 0
    while not pq.empty():
        w, u = pq.get()
        visited[u] = True
        for v in range(n):
            w = graph[u][v]
            if not visited[v] and dist[v] > w:
                dist[v] = w
                pq.put((w, v))

def solve():
  while True:
  #     try:
      n = int(Scanner.next())
      buildings = [None] * n
      for i in range(n):
          buildings[i] = (int(Scanner.next()), int(Scanner.next()))
          
      graph = [[INF] * n for i in range(n)]

      dist = [INF for i in range(n)]
      visited = [False for i in range(n)]

      # print(dist)

      m = int(Scanner.next())

      for k in range(m):
          a, b = int(Scanner.next()), int(Scanner.next())
          graph[a - 1][b - 1] = 0
          graph[b - 1][a - 1] = 0

      # O(n^2)
      for i in range(n):
          for j in range(i + 1, n):
            if graph[i][j] != 0:
              curr_dist = math.sqrt(
                  (buildings[i][1] - buildings[j][1])**2 + (buildings[i][0] - buildings[j][0])**2)
              graph[i][j] = curr_dist
              graph[j][i] = curr_dist
  #             graph[i].append(Node(j, curr_dist))
  #             graph[j].append(Node(i, curr_dist))
      # O(n log n)
      prim(0, graph, dist, visited)
      print("{0:.2f}".format(sum(dist)))

solve()
