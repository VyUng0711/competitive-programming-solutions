from queue import Queue 
 
def one_e_point(m):
  count=0
  for i in range(len(m)):
    for j in range(len(m[0])):
      if i == 0 or i == len(m)-1 or j == 0 or j == len(m[0])-1:
        if m[i][j] == '.':
          count+=1
          if count==1:
            entrance_x, entrance_y = (i,j)
          if count==2:
            exit_x, exit_y = (i,j)      
  if count==2:
    return ((entrance_x, entrance_y),(exit_x,exit_y))
  else:
    return False     
   
def bfs(x, y, x_out, y_out, m):
  visit = [[False] * len(m[0]) for i in range(len(m))]
  q = Queue()
  visit[x][y] = True
  q.put((x,y))
  while q.empty() == False: 
    x,y = q.get()
    dir = [(0,-1),(-1,0),(0,1),(1,0)]
    for dx, dy in dir:
      new_x = x + dx
      new_y = y + dy
      if new_x == x_out and new_y == y_out:
        return True
      if new_x < len(m) and new_y < len(m[0]) and new_x>=0 and new_y>=0 and m[new_x][new_y]=='.':
        if visit[new_x][new_y]==False:
          visit[new_x][new_y]=True
          q.put((new_x,new_y))
  return False
      
def check_valid(m):
  if one_e_point(m) == False:
    return 'invalid'
  else:
    s, f = one_e_point(m)
    if bfs(s[0],s[1],f[0],f[1],m):
      return 'valid'
    else:
      return 'invalid'
 
t = int(input())
for k in range(t):
  m, n = map(int, input().split())
  s = []
  for i in range(m):
    s.append(input())
  print (check_valid(s))