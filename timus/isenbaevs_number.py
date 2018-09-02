from collections import defaultdict
from queue import Queue
INF = float('inf')
# http://acm.timus.ru/problem.aspx?space=1&num=1837
mapping = defaultdict(list)

n = int(input())
# O(n)
for i in range(n):
  team = input().split()
  for i in range(len(team)):
    for j in range(len(team)):
      if i != j:
        mapping[team[i]].append(team[j])
  
visited = {m: False for m in mapping.keys()}
dist = {m: INF for m in mapping.keys()} 

# O(V + E)
# V ~ n * 3
# E ~ n * 3 * 2
# O(n)
def bfs(s):
  q = Queue()
  visited[s] = True
  q.put(s)
  dist[s] = 0
  while not q.empty():
    u= q.get()
    for v in mapping[u]:
      if visited[v] == False:
        visited[v] = True
        q.put(v)
        dist[v] = dist[u] + 1
if 'Isenbaev' in mapping:
  bfs('Isenbaev')

# O(n * log (n))
for k, v in sorted(dist.items()):
  if v != INF:
    print(k, v)
  else:
    print(k, 'undefined')
