from queue import Queue
n, m = [int(x) for x in input().split()]
cats = [int(x) for x in input().split()]
graph = [[] for i in range(n)]
for edge in range(n-1):
  v1, v2 = map(int, input().strip().split(' '))
  graph[v1-1].append(v2-1)
  graph[v2-1].append(v1-1)


def bfs(n, m, cats, graph):
  count_path = 0
  visited = [False]*n
  path = [-1]*n
  q = Queue()
  visited[0]=True
  q.put(0)
  path[0]=cats[0]
  while q.empty() == False:
    u = q.get()
    for i in graph[u]:
      if visited[i] == False:
        visited[i] = True
        if cats[i] == 1:
          path[i] = path[u] + cats[i]
        else:
          path[i] = 0
        if path[i] > m:
          continue 
        else:
          if len(graph[i]) == 1 and i != 0:
            count_path +=1
        q.put(i)
  return count_path
print (bfs(n, m, cats, graph))