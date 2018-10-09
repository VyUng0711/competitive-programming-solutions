# https://www.spoj.com/problems/LOSTNSURVIVED/
import queue

def findSet(u):
  if parents[u] != u:
    parents[u] = findSet(parents[u])
  return parents[u]

def unionSet(u, v):

  up = findSet(u)
  vp = findSet(v)
  if up == vp:
    return size[up]
  if ranks[up] > ranks[vp]:
    parents[vp] = up
    size[up] += size[vp]
    # update size[up] in pq
    pq.put((size[up], up))
    size[vp] = 0
    return size[up]
  elif ranks[up] < ranks[vp]:
    parents[up] = vp
    size[vp] += size[up]
    
    pq.put((size[vp], vp))
    size[up] = 0
    return size[vp]
  else:
    parents[up] = vp
    ranks[vp] += 1
    size[vp] += size[up]
    pq.put((size[vp], vp))
    size[up] = 0
    
    return size[vp]
    

n, q = map(int, input().split())
parents = [i for i in range(n)]
ranks = [0 for i in range(n)]
size = {i : 1 for i in range(n)}
pq = queue.PriorityQueue()
for i in range(n):
  pq.put((1, i))

max_so_far = 0

for i in range(q):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  this_size = unionSet(a, b)
  max_so_far = max(this_size, max_so_far)
  while pq.qsize():
    sizeu, u = pq.queue[0]
    if sizeu != size[u]:
      pq.get()
    else:
      break
  print(max_so_far - pq.queue[0][0])
