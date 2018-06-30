class Scanner():
    def __generator__():
        while True:
            buffer = input().strip().split()
            for x in buffer:
                yield x
    scanner = __generator__()
    def next():
        return Scanner.scanner.__next__()

n = int(Scanner.next())
m = int(Scanner.next())
graph = [[] for x in range(n)]
for i in range(m):
  u = int(Scanner.next())
  v = int(Scanner.next())
  graph[u-1].append(v-1)
  
def possible_impact(graph, start):
  visited = [False] * n
  stack = []
  stack.append(start)
  visited[start]=True
  count = 1
  while len(stack) > 0:
    cur = stack.pop()
    for i in graph[cur]:
      if visited[i] == False:
        stack.append(i)
        visited[i] = True
        count += 1
  return count

max_impact = 0
for node in range(n):
  cur_impact = possible_impact(graph, node)
  max_impact = max(cur_impact, max_impact)
print (max_impact)
  