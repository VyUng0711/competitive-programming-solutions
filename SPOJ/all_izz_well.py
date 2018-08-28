# https://www.spoj.com/problems/ALLIZWEL/
import sys
sys.setrecursionlimit(1000000)
num_test_cases = int(input())
for test_case in range(num_test_cases):
  r, c = map(int, input().split())
  matrix = [[] for j in range(r)]
  #print (matrix)
  for irow in range(r):
    this_row = input()
    #print (this_row[5])
    for item in this_row:
      matrix[irow].append(item)
#   print (matrix)
  
  possible_starts = []
  for i in range(r):
    for j in range(c):
      if matrix[i][j] == 'A':
        possible_starts.append((i, j))


  MOVES = [(0, 1), (1, 1), (1, 0), (1, -1),
          (0, -1), (-1, -1), (-1, 0), (-1, 1)]

  EXPECTED = "ALLIZZWELL"
  cursor = 0
  visited = [[False]*c for i in range(r)]
#   print (visited)

  def find_path(graph, sx, sy):
  #   print(sx, sy)
    global cursor
    visited[sx][sy] = True
    cursor += 1
  #   print ("cursor", cursor)
    if cursor == len(EXPECTED):
      return True 
    for dx, dy in MOVES:
      new_x = sx + dx
      new_y = sy + dy
      #print ((new_x, new_y))
      if new_x >= 0 and new_y >= 0 and new_x < len(graph) and new_y < len(graph[0]):
        if visited[new_x][new_y] == False and graph[new_x][new_y] == EXPECTED[cursor] :
  #         print ("recurse")
          if find_path(graph, new_x, new_y):
            return True

    cursor -= 1 
    visited[sx][sy] = False
    return False

#   print (find_path(matrix, 0, 0))

  result = "NO"
  for start_x, start_y in possible_starts:
#     print(start_x, start_y, cursor)
    if find_path(matrix, start_x, start_y):
      result = "YES"
      break
  print (result)
  if test_case < num_test_cases - 1:
    input()


  
  
