# https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/dhoom-4/
from queue import Queue
path = [-1]*100001
def bfs(start, target, keys):
  q = Queue()
  path[start] = 0
  q.put(start)
  while q.empty() == False:
    u = q.get()
    if u == target:
      return (path[u])
    for k in keys:
      v = (u*k) % 100000
      if path[v] == -1:
        q.put(v)
        path[v] = path[u] + 1
  return (path[target])

start, target = map(int, input().split())
n = int(input())
keys=[int(x) for x in input().split()]
print(bfs(start, target,keys))
