from queue import Queue
"""
input = [[1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,0,0,0,0,0,0],
        [1,1,1,0,0,0,0,1,1,1],
        [1,1,0,0,1,0,0,1,1,1],
        [1,0,1,0,0,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1]]
"""
DIR = [(0, -1), (-1, 0), (0, 1), (1, 0)]
# return slick's size
def bfs(x, y, s):
  q = Queue()
  count = 0 
  q.put((x,y))
  s[x][y]=0
  while q.empty()==False:
    x, y = q.get()
    count+=1
    for dx, dy in DIR:
      new_x = x + dx
      new_y = y + dy
      if new_x < len(s) and new_x >= 0 and new_y < len(s[0]) and new_y >= 0:
        if s[new_x][new_y] == 1:
          q.put((new_x, new_y))
          s[new_x][new_y] = 0
  return count

def slick(s,n,m):
  dict = {}
  for i in range(n):
    for j in range(m):
      if s[i][j] == 1:
        size = bfs(i, j, s)
        if size not in dict:
          dict[size] = 1
        else:
          dict[size] += 1
  sorted_keys = sorted(dict.keys())
  print (sum(dict.values()))
  for k in sorted_keys:
    print (k, dict[k])

while True:
  n, m = map(int, input().split())
  if n==0 and m==0:
    break
  grid = []
  for i in n:
    this_line = list(map(int,input().split()))
    grid.append(this_line)
    
  slick(grid, n, m)  

 
    
      