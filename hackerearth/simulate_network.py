# https://www.hackerearth.com/fr/challenge/hiring/globalsoft-backend-hiring-challenge/algorithm/efficient-network/description/
import queue
INF = float('inf')

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist
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
            if not visited[v] and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u
def printMST():
    ans = 0
    for i in range(n):
        if path[i] == -1:
            continue
        ans += dist[i]
        print("{} - {}: {}".format(path[i], i, dist[i]))
    return ans
    
n, m = map(int, input().split())
graph = [[] for i in range(n)]
dist = [INF for i in range(n)]
path = [-1 for i in range(n)]
visited = [False for i in range(n)]
for i in range(m):
    u, v, w = map(int, input().split())
    graph[u - 1].append(Node(v - 1, w))
    graph[v - 1].append(Node(u - 1, w))
q = int(input())
if q > 0:
    cables = list(map(int, input().split()))
else:
    cables = []

prim(0)
# print(dist)
new_cables = dist + cables
sorted_cables = sorted(new_cables)
# print(sorted_cables[:n])
cost = sum(sorted_cables[:n])
print(cost)
# printMST()
    
    
    
