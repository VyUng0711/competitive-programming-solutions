# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1168

def findSet(u):
  if parent[u] != u:
    parent[u] = findSet(parent[u])
  return parent[u]

def unionSet(u, v):
  up = findSet(u)
  vp = findSet(v)
  if up == vp:
    return
  if ranks[up] > ranks[vp]:
    parent[vp] = up

  elif ranks[up] < ranks[vp]:
    parent[up] = vp

  else:
    parent[up] = vp
    ranks[vp] += 1


num_test = int(input())
blankline = input()


for t in range(num_test):
  num_people, num_tree = map(int, input().split())
  graph = [set() for _ in range(num_people)]
  parent = [i for i in range(num_people)]
  ranks = [0 for i in range(num_people)]
  
  
  
  while True:
    try:
      this_line = input()
      # print(this_line)
      if this_line != '':
        i, j = map(int, this_line.split())
        i -= 1
        j -= 1
        graph[i].add(j)
        
        # print(i, j)
      if this_line == '':
        break
    except EOFError:
      break
      
  print(graph)
  for i in range(len(graph) - 1):
    for j in range(i + 1, len(graph)):
      if graph[i] == graph[j]:
        unionSet(parent[i], parent[j])
  count = 0
  for k in range(len(parent)):
    if k == parent[k]:
      count += 1
  print(count)
  print()
        
     
