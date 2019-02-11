# https://www.spoj.com/problems/UCI2009D/

import copy
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(sx, sy, length, path):
  # (8 ^ 2 * 4 ^ 7)
  global count
  if length == 8:
    count += 1
    # print(sorted(path))
    res.add(str(sorted(path)))
    return

  visited[sx][sy] = True

  for dx, dy in DIR:
    x = sx + dx
    y = sy + dy
    if x >= 0 and y >= 0 and x < n and y < n:
      if not visited[x][y] and grid[x][y] == "X":
        # visited[x][y] = True
        path.append((x, y))
        dfs(x, y, length + 1, path)
        path.pop()
        # visited[x][y] = False
  
  visited[sx][sy] = False
  return

num_test = int(input())
for t in range(num_test):
  n = int(input())
  grid = []
  for i in range(n):
    row = []
    line = input()
    for j in line:
      row.append(j)
    grid.append(row)
  # print(grid)
  visited = [[False] * n for _ in range(n)]
  res = set()
  count = 0
  for i in range(n):
    for j in range(n):
      if grid[i][j] == 'X':
        dfs(i, j, 1, [(i, j)])
  # print(count)
  print(len(res))
  # print(res)
