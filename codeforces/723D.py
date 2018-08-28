# http://codeforces.com/problemset/problem/723/D
import operator
import copy
n, m, k = map(int, input().split())
map = [None] * n 
for _ in range(n):
  map[_] = list(input().strip())
edited_map = copy.deepcopy(map)

DIR = [(0,-1),(-1,0),(0,1),(1,0)]
def dfs(source_x, source_y, map):
  this_size = 1
  stack = []
  stack.append((source_x, source_y))
  map[source_x][source_y] = '*'
  lake_area = []
  lake_area.append((source_x, source_y))
  is_ocean = False
  while len(stack) > 0:
    x, y = stack.pop()
    for dx, dy in DIR:
      new_x = x + dx
      new_y = y + dy
      if new_x < len(map) and new_y < len(map[0]) \
      and new_x >= 0 and new_y >= 0:
        if map[new_x][new_y] == '.':
          stack.append((new_x, new_y))
          this_size += 1
          map[new_x][new_y]='*'
          lake_area.append((new_x, new_y))
      else:
        is_ocean = True
        return ((-1, ()))
  lake_area = tuple(lake_area)
  return ((this_size, lake_area))

lakes = {}
for i in range(n):
  for j in range(m):
    if map[i][j] == '.':
      result = dfs(i,j,map)
      size = result[0]
      area = result[1]
      if size != -1:
        lakes[area] = size
#print (lakes)
sorted_lake = sorted(lakes.items(), key=operator.itemgetter(1))
#print (sorted_lake)
num_fill = len(sorted_lake) - k
print (num_fill)
count = 0
for key in sorted_lake:
  if count == num_fill:
    break
  for cell in key[0]:
    edited_map[cell[0]][cell[1]]='*'
  count+=1
#print (edited_map)
for row in edited_map:
  for item in row:
    print (item, end='')
  print()
  
  
  
  
  

      