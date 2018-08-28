# http://www.spoj.com/problems/ABCPATH/
import sys
sys.setrecursionlimit(1000000)
def find_path(graph, sx, sy):
  if dist[sx][sy] != 0:
    return dist[sx][sy]
  dist[sx][sy] = 1
  this_value = ord(graph[sx][sy])
  for dx, dy in MOVES:
    new_x = sx + dx
    new_y = sy + dy
    if new_x >= 0 and new_y >= 0 and new_x < len(graph) and new_y < len(graph[0]):
      new_value = ord(graph[new_x][new_y])
      #print ((new_x, new_y))
      if new_value - this_value == 1:
        dist[sx][sy] = max(dist[sx][sy], find_path(graph, new_x, new_y) + 1)
  return dist[sx][sy]
  

case = 1
while True:
  h, w = map(int, input().split())
  if h == 0 and w == 0:
    break
  grid = [[] for r in range(h)]
  start_positions = []
  for row_index in range(h):
    this_row = input().strip()
    col_index = 0
    for item in this_row:
      grid[row_index].append(item)
      if ord(item) == 65:
        start_positions.append((row_index, col_index))
      col_index+=1
  #print (grid)
  #print (start_positions)
  
  MOVES = [(0, 1), (1, 1), (1, 0), (1, -1),
          (0, -1), (-1, -1), (-1, 0), (-1, 1)]
  dist = [[0]*w for _ in range(h)]
  visited = [[False]*w for _ in range(h)]
#   print (visited)
  possible_max_counts = [0]
  for start_x, start_y in start_positions:
    find_path(grid, start_x, start_y)
    possible_max_counts.append(dist[start_x][start_y])
  print ("Case {}: {}".format(case, max(possible_max_counts)))
  case+=1 



