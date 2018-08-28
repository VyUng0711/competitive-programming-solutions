# https://www.urionlinejudge.com.br/judge/en/problems/view/1610
def find_one_loop(source, graph, n):
  stack = []
  stack.append(source)
  visited = [False] * n 
  while len(stack) > 0: 
    u = stack.pop()
    #print (u)
    for v in graph[u]:
      if visited[v] == False:
        visited[v] = True
        stack.append(v)
        if v == source:
          return True
  return False


#print (find_one_loop(0,[[1],[0]]))

def find_all_loop(n, graph):
  for j in range(n):
    this_loop = find_one_loop(j, graph, n)
    if this_loop == True:
      return ("SIM")
  return ("NAO")

#print (find_all_loop(2,[[1],[0]]))
#print (find_all_loop(2,[[1],[]]))
#print (find_one_loop(0, [[2],[2],[3],[1]], 4))
#print (find_all_loop(4, [[2],[2],[3],[1]]))
      
t = int(input())
for j in range(t):
  n, m = map(int, input().split())
  this_graph = [[] for i in range(n)]
  for i in range(m):
    u, v = map(int, input().split())
    this_graph[u-1].append(v-1)
    
  print (find_all_loop(n, this_graph))
