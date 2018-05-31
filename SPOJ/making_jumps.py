case = 0
while True:
  case += 1
  board = []
  line = list(map(int, input().split()))
  if line[0] == 0:
    break
  for i in range(line[0]):
    start, length = line[i * 2 + 1], line[i * 2 + 2]
    for j in range(length):
      board.append((i, start+j))

  MOVES = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
           (1, -2), (1, 2), (2,-1), (2, 1)]

  visited = [[False] * 10 for i in range(10)]
  cnt = 0
  max_cnt = 0
  def possible_moves(board, sx, sy):
    global cnt, max_cnt
    visited[sx][sy] = True
    cnt += 1
    max_cnt = max(max_cnt, cnt)
    for dx, dy in MOVES:
        new_x = sx + dx
        new_y = sy + dy
        if visited[new_x][new_y] == False and \
        (new_x, new_y) in board:
          print ((new_x, new_y))
          possible_moves(board, new_x, new_y)
  #         possible_moves(board, new_x', new_y')
    cnt -= 1
    visited[sx][sy] = False
  possible_moves(board, 0, 0)
  #print (len(board))
  result = len(board)-max_cnt
  if result == 1: 
    print ("Case {}, {} square can not be reached.".format(case, result))
  else:
    print ("Case {}, {} squares can not be reached.".format(case, result))
    



