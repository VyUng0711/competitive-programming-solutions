
def findSet(u):
  if parent[u] != u:
    parent[u] = findSet(parent[u])
  return parent[u]

def unionSet(u, v):
  up = findSet(u)
  vp = findSet(v)
  if up == vp:
    return
  if ranks[up] > ranks[vp]:
    parent[vp] = up
  elif ranks[up] < ranks[vp]:
    parent[up] = vp
  else:
    parent[up] = vp
    ranks[vp] += 1

n, m = map(int, input().split())
# mapping = {}
# graph = [None] * n

parent = [i for i in range(n + m)]
ranks = [0 for i in range(n + m)]


# Complexity: n * m * log(n + m)
for i in range(n):
  this_emp = list(map(int, input().split()))
  if this_emp[0] > 0:
    for j in this_emp[1:]:
      unionSet(i, j - 1 + n)

cost = 0
for k in range(n + m):
  if parent[k] == k:
    cost += 1

print(cost - 1)
print(parent)



# Complexity: O(n*n*m*log(n))
for i in range(n):
  this_emp = list(map(int, input().split())) 
  # mapping[i] = this_emp[1:]
  if this_emp[0] == 0:
    graph[i] = []
  else:
    graph[i] = this_emp[1:]
# print(graph)

parent = [i for i in range(n)]
ranks = [0 for i in range(n)]
# cost = n


for i in range(len(graph)): # O(n)
  for j in range(i + 1, len(graph)): # O(n)
    if ((set(graph[i]) & set(graph[j]))): # O(m)
      unionSet(i, j) # O(log n)
      # cost = cost - 1

# print(cost)
cost = 0
for p in range(len(parent)):
  if p == parent[p]:
    cost += 1

# print(parent)
empty = 0
for i in range(len(graph)):
  if len(graph[i]) == 0:
    empty += 1
    
if empty == n:
  print(n)
else:
  print(cost - 1)


