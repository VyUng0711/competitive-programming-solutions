# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1338
import math
import queue
INF = float('inf')
class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return(self.dist <= other.dist)
     
def prim(source):
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
            if not visited[v] and dist[v] > w:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u
                
while True:
    try:
        n = int(input())
        b = []
        for _ in range(n):
            x, y = map(int, input().split())
            b.append((x, y))
        graph = [[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    curr_dist = math.sqrt(
                        (b[i][1] - b[j][1])**2 + (b[i][0] - b[j][0])**2)
                    graph[i].append(Node(j, curr_dist))
                    graph[j].append(Node(i, curr_dist))
        dist = [INF for i in range(n)]
        path = [-1 for i in range(n)]
        visited = [False for i in range(n)]
        prim(0)
        # print(dist)
        m = int(input())
        available = set()
        for k in range(m):
            a, b = map(int, input().split())
            available.add((a - 1, b - 1))
            available.add((b - 1, a - 1))
        total = 0
        for i in range(n):
            if (i, path[i]) in available:
                continue
            else:
                total += dist[i]
        print("{0:.2f}".format(total))
                
            
    except EOFError:
        break
    
