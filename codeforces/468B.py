# http://codeforces.com/contest/468/problem/B
def findSet(u):
  if parents[u] != u:
    parents[u] = findSet(parents[u])
  return parents[u]


def unionSet(u, v):
  up = findSet(u)
  vp = findSet(v)
  if up == vp:
    return
  
  if ranks[up] > ranks[vp]:
    parents[vp] = up
  elif ranks[up] < ranks[vp]:
    parents[up] = vp
  else:
    parents[up] = vp
    ranks[vp] += 1
    
n, a, b = map(int, input().split())
ps = list(map(int, input().split())) 

mapping = set(ps)

parents = {x: x for x in ps}
parents['A'] = 'A'
parents['B'] = 'B'
ranks = {x: 0 for x in ps}
ranks['A'] = 0
ranks['B'] = 0

result = True
for x in ps:
  if a - x in mapping:
    unionSet(x, a - x)
  else:
    unionSet(x, 'B')
    
  if b - x in mapping:
    unionSet(x, b - x)
  else:
    unionSet(x, 'A')

if findSet('A') == findSet('B'):
  print("NO")
  
else:
  print("YES")
  for i in ps:
    if findSet(i) == findSet('A'):
      print("0", end = ' ')
    else:
      print("1", end = ' ')


# Instead of using dictionary, we can map the number into index:
def findSet(u):
  if parents[u] != u:
    parents[u] = findSet(parents[u])
  return parents[u]


def unionSet(u, v):
  up = findSet(u)
  vp = findSet(v)
  if up == vp:
    return
  
  if ranks[up] > ranks[vp]:
    parents[vp] = up
  elif ranks[up] < ranks[vp]:
    parents[up] = vp
  else:
    parents[up] = vp
    ranks[vp] += 1
    
n, a, b = map(int, input().split())
ps = list(map(int, input().split())) 


mapping = {}

for i in range(n):
  mapping[ps[i]] = i
  
parents = [i for i in range(n + 2)]
print(parents)
ranks = [0 for i in range(n + 2)]

for i in range(n):
  if a - ps[i] in mapping:
    unionSet(i, mapping[a - ps[i]])
  else:
    unionSet(i, n + 1)
    
  if b - ps[i] in mapping:
    unionSet(i, mapping[b - ps[i]])
  else:
    unionSet(i, n)
  print(parents)
  
print(parents)
print(findSet(n))
print(findSet(n + 1))

if findSet(n) == findSet(n + 1):
  print("NO")
else:
  print("YES")
  for i in range(n):
    if findSet(i) == findSet(n):
      print("0", end = ' ')
    else:
      print("1", end = ' ')


