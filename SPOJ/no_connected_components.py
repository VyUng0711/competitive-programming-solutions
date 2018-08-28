#  https://www.spoj.com/problems/CCOMPS/
def dfs(n, edge, graph, path, source):
  stack = []
  stack.append(source)
  while len(stack) > 0:
    u = stack[-1]
    stack.pop()
    for v in graph[u]:
      if path[v] == -1 and v != source:
        stack.append(v)
        path[v] = u

t = int(input())

for i in range(t):
  n = int(input())
  e = int(input())
  graph = [[] for i in range(n)]
  for j in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
  path = [-1]*n
  for j in range(n):
    if path[j] == -1:
      dfs(n, e, graph, path, j)
      
  result = 0 
  for p in path:
    if p == -1:
      result += 1
  print (result)
  


        
      
              
    
  
  
  