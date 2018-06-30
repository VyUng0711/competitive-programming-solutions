from queue import Queue
DIR = [(0, -1), (-1, 0), (0, 1), (1, 0)]
def bfs(r1, c1, r2, c2, cave):
  q = Queue()
  q.put((r1, c1))
  while q.empty() == False:
    x, y = q.get()
    for dx, dy in DIR:
      new_x = x + dx
      new_y = y + dy
      if new_x < len(cave) and new_y < len(cave[0]) \
      and new_x >= 0  and new_y >= 0:
        if cave[new_x][new_y] == 'X':
          if new_x == r2 and new_y == c2:
            return 'YES'
          else:
            continue
        else:
          q.put((new_x, new_y))
          cave[new_x][new_y] = 'X'
  return 'NO'

n, m = map(int, input().split())
cave = [None] * n
for i in range(n):
  cave[i] = list(input())
   
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
print (bfs(r1 - 1, c1 - 1, r2 - 1, c2 - 1, cave))

