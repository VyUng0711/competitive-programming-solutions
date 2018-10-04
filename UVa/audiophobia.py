# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=989
# Using Prim together with DFS/BFS. Complexity: O(t * s * log(c)) + O(t * q * (s + c))
import queue
INF = float('inf')
class Node:
  def __init__(self, id, dist):
    self.id = id
    self.dist = dist
  def __lt__(self, other):
    return self.dist <= other.dist
  

def prim(source):   # O (s * log(c))
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
  # print(path)
  # print(dist)
  for p in range(len(path)):
    if path[p] != -1:
      mst[p].append(Node(path[p], dist[p]))
      mst[path[p]].append(Node(p, dist[p]))
  return mst


def dfs(start, target, mst):    # O (s + c)
  visited = [False] * len(mst)
  dist = [-INF for i in range(len(mst))]       
  stack = []
  visited[start] = True
  stack.append(Node(start, 0))
  while len(stack) > 0:
    top = stack.pop()
    u = top.id
    if u == target:
      return dist[u]
    for v in mst[u]:
      if visited[v.id] == False:
        visited[v.id] = True
        stack.append(v)
        dist[v.id] = max(dist[u], v.dist)
  if dist[target] == -INF:
    return "no path"
  return dist[target]
  
  
case_no = 1

while True:
  c, s, q = map(int, input().split())
  if c == 0 and s == 0 and q == 0:
    break
  if case_no != 1:
    print()
  graph = [[] for i in range(c)]
  
  for i in range(s):
    c1, c2, d = map(int, input().split())
    graph[c1 - 1].append(Node(c2 - 1, d))
    graph[c2 - 1].append(Node(c1 - 1, d))
  
  queries = []
  for j in range(q):
    q1, q2 = map(int, input().split())
    queries.append((q1 - 1, q2 - 1))

  print("Case #{}".format(case_no))
  case_no += 1

  mst = [[] for i in range(c)]
  dist = [INF for i in range(c)]
  visited = [False for i in range(c)]
  path = [-1 for i in range(c)]
  # sum(si * log(ci)) ~ O(s * log(c))
  for i in range(c):
    if path[i] == -1:
      prim(i)
  # O (q * (s + c))
  for q1, q2 in queries:
    result = dfs(q1, q2, mst)
    print(result)



# Using dynamic programming. Complexity: O(t * q * s * log(c))
import queue
INF = float('inf')
class Node:
  def __init__(self, id, dist):
    self.id = id
    self.dist = dist
  def __lt__(self, other):
    return self.dist <= other.dist

def dp(start, target):
  dist = [INF for i in range(c)]
#   visited = [False for i in range(c)]
  pq = queue.PriorityQueue()
  pq.put(Node(start, 0))
  dist[start] = 0
  while not pq.empty():
    top = pq.get()
    u = top.id
#     visited[u] = True
    for neighbor in graph[u]:
      v = neighbor.id
      w = neighbor.dist 
      if max(w, dist[u]) < dist[v]:
        dist[v] = max(w, dist[u])
        pq.put(Node(v, w))    
  return dist[target]


case_no = 1
# O(t * q * c * log(s))
while True:
  c, s, q = map(int, input().split())
  if c == 0 and s == 0 and q == 0:
    break
  if case_no != 1:
    print()
  graph = [[] for i in range(c)]
  
  for i in range(s):
    c1, c2, d = map(int, input().split())
    graph[c1 - 1].append(Node(c2 - 1, d))
    graph[c2 - 1].append(Node(c1 - 1, d))
  
  queries = []
  # O(q * c * log(s))
  for j in range(q):
    q1, q2 = map(int, input().split())
    queries.append((q1 - 1, q2 - 1))

  print("Case #{}".format(case_no))
  case_no += 1
  for q1, q2 in queries:
    result = dp(q1, q2)
    if result == INF:
      print("no path")
    else:
      print(result)

