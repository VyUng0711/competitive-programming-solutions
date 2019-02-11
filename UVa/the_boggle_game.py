# https://uva.onlinejudge.org/index.php?option=onlinejudge&Itemid=99999999&page=show_problem&category=&problem=545&mosmsg=Submission+received+with+ID+22546025

def find_word(board, sx, sy):
  res = set()
  visited = [[False] * 4 for _ in range(4)]

  MOVES = [(0, 1), (1, 1), (1, 0), (1, -1),
            (0, -1), (-1, -1), (-1, 0), (-1, 1)]

  VOWELS = {'E', 'A', 'U', 'Y', 'I', 'O'}

  def dfs(board, sx, sy, word):
    word.append(board[sx][sy])

    if len(word) == 4:
      count_v = 0
      for i in range(4):
        if word[i] in VOWELS:
          count_v += 1
      if count_v == 2:
        res.add(''.join(word))
      word.pop()
      return
    
    
    
    visited[sx][sy] = True

    for dx, dy in MOVES:
      new_x = sx + dx
      new_y = sy + dy
      if new_x >= 0 and new_y >= 0 and new_x < 4 and new_y < 4:
        if not visited[new_x][new_y]:
          dfs(board, new_x, new_y, word)

    visited[sx][sy] = False
    word.pop()

  dfs(board, sx, sy, [])
  return res

stop = False 
first_case = True
while True:
  
  first = []
  second = [] 
  while True:
    this_line = input()
    if this_line == "#":
      stop = True
      break
    if this_line == "":
      break
    this_line = list(this_line.split())
    first.append(this_line[:4])
    second.append(this_line[4:])
  if stop:
    break

  if not first_case:
    print()
  first_case = False

  # W ~ max num of words --> O(W)
  # T ~ num testcase
  # Complexity: O( T * W)
  # DFS:  ~ 6 x 8 x 7 x 7 ~ 6000
  first_res = set()
  second_res = set()
  for i in range(4):
    for j in range(4):
      first_res.update(find_word(first, i, j))
      second_res.update(find_word(second, i, j))
  # print(first_res)
  # print(second_res)
  res = first_res.intersection(second_res)
  if len(res) == 0:
    print("There are no common words for this pair of boggle boards.")
  else:
    for w in sorted(list(res)):
      print(w)
