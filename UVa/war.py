# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1099

def findSet(u):
  if parent[u] != u:
    parent[u] = findSet(parent[u])
  return parent[u]

def setFriends(x, y):
  xp = findSet(x)
  yp = findSet(y)
  if xp == yp:
    return True
  if xp == -yp:
    # print(-1)
    return False
  
  if ranks[xp] > ranks[yp]:
    parent[yp] = xp
  elif ranks[xp] < ranks[yp]:
    parent[xp] = yp
  else:
    parent[xp] = yp
    ranks[yp] += 1
  return True
    
def areFriends(x, y):
  xp = findSet(x)
  yp = findSet(y)
  if xp == yp:
    return True
  else:
    return False
  


n = int(input())
parent = {i: i for i in range(-n, n + 1) if i != 0}
ranks = {i: 0 for i in range(-n, n + 1) if i != 0}

# index = 1
while True:
  
  # print('index', index)
  c, x, y = map(int, input().split())
  if c == 0 and x == 0 and y == 0:
    break
  x += 1
  y += 1
  # print(x)
  # print(y)
  if c == 1:
    if not setFriends(-x, -y) or not setFriends(x, y):
      print('-1')
      
    else:
      setFriends(-x, -y)
      setFriends(x, y)
      
  elif c == 2:
    if not setFriends(x, -y) or not setFriends(-x, y):
      print('-1')
    else:
      setFriends(x, -y)
      setFriends(-x, y)
      
  elif c == 3:
    if areFriends(x, y) and areFriends(-x, -y):
      print('1')
    else:
      print('0')
  elif c == 4:
    if areFriends(x, -y) and areFriends(y, -x):
      print('1')
    else:
      print('0')
  # index += 1
  
