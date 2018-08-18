import queue
def bfs(sy, sx, ty, tx):
    q = queue.Queue()
    q.put((sy, sx))
    distance[sy][sx] = 0
    while not q.empty():
      y, x = q.get()
      for dy, dx in DIR:
        new_y = y + dy
        new_x = x + dx
        if new_y >= 0 and new_x >= 0 and new_y < len(graph) and new_x < len(graph[0]):
          if (new_y, new_x) not in bomb_ids:
            if distance[new_y][new_x] == -1:
              q.put((new_y, new_x))
              distance[new_y][new_x] = distance[y][x] + 1
              if new_y == ty and new_x == tx:
                return distance[new_y][new_x]

while True:
  row, col = map(int, input().split())
  if row == 0 and col == 0:
    break
  graph = [[]*col for _ in range(row)]
  for r in range(row):
    for c in range(col):
      graph[r].append(c)
  # print(graph)
  num_row_with_bombs = int(input())
  bomb_ids = []
  for rb in range(num_row_with_bombs):
    this_row = list(map(int, input().split()))
    row_id = this_row[0]
    num_bombs = this_row[1]
    for col_id in range(2, len(this_row)):
      bomb_ids.append((row_id, this_row[col_id]))
  sy, sx = map(int, input().split())
  dy, dx = map(int, input().split())
  DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]
  distance = [[-1] * col for _ in range(row)]
  print(bfs(sy, sx, dy, dx))