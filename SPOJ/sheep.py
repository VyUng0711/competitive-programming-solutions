from queue import Queue
DIR = [(0, -1), (-1, 0), (0, 1), (1, 0)]
def bfs(start_x, start_y, yard):
  num_sheep = 0
  num_wolves = 0
  q = Queue()
  q.put((start_x,start_y))
  
  if yard[start_x][start_y] == 'k':
    num_sheep += 1
  if yard[start_x][start_y] == 'v':
    num_wolves += 1
  yard[start_x][start_y] = '#'
  
  outer_field = False
  
  while q.empty() == False:
    x, y = q.get()
    for dx, dy in DIR:
      new_x = x + dx
      new_y = y + dy
      if new_x < len(yard) and new_y < len(yard[0]) \
      and new_x >= 0 and new_y >= 0:
        if yard[new_x][new_y] != '#':
          q.put((new_x,new_y))
          if yard[new_x][new_y] == 'k':
            num_sheep += 1
          if yard[new_x][new_y] == 'v':
            num_wolves += 1
          yard[new_x][new_y]='#'
      else:
        outer_field = True
        
  if not outer_field:  
    if num_sheep > num_wolves:
      num_wolves = 0
    else:
      num_sheep = 0
  return (num_sheep, num_wolves)

def count_total(n, m, yard):
  total_sheep = 0
  total_wolves = 0
  for i in range(n):
    for j in range(m):
      if yard[i][j] != '#':
        num_sheep, num_wolves = bfs(i,j,yard)
        total_sheep += num_sheep
        total_wolves += num_wolves
  return (total_sheep, total_wolves)
        
line = ''
while line == '':
  line = input().strip()
n, m = map(int, line.split())
yard = [None] * n
for i in range(n):
  yard[i] = list(input().strip())
#print (yard)
print (*count_total(n, m, yard))

    