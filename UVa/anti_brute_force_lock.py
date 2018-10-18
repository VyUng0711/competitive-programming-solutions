# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3676
class Triad():
  def __init__(self, source, target, weight):
    self.source = source
    self.target = target
    self.weight = weight
    
def findSet(u):
  if parents[u] != u:
    parents[u] = findSet(parents[u])
  return parents[u]

def unionSet(u, v):
  up = findSet(u)
  vp = findSet(v)
  if up == vp:
    return
  if ranks[up] > ranks[vp]:
    parents[vp] = up
  elif ranks[vp] > ranks[up]:
    parents[up] = vp
  else:
    parents[up] = vp
    ranks[vp] += 1
    
def kruskal():
  global min_num_rolls
  graph.sort(key= lambda edge: edge.weight)
  i = 0
  while len(dist) != n - 1:
    edge = graph[i]
    i += 1
    up = findSet(edge.source)
    vp = findSet(edge.target)
    if up != vp:
      dist.append(edge)
      unionSet(up, vp)
      min_num_rolls += edge.weight
      
def get_num_rolls(a, b):
  num_rolls = 0
  for i in range(len(a)):
    if int(a[i]) < int(b[i]):
      num_rolls += min(int(b[i]) - int(a[i]), int(a[i]) + 10 - int(b[i]))
    elif int(a[i]) > int(b[i]):
      num_rolls += min(int(a[i]) - int(b[i]), int(b[i]) + 10 - int(a[i]))
      
  return num_rolls


num_test = int(input())
for t in range(num_test):
  this_case = input().split()
  n = int(this_case[0])
  # print('n', n)
  keys = this_case[1:]
  # keys.append('0000')
  # print(keys)
  from_zero = [get_num_rolls('0000', x) for x in keys]
  min_from_zero = min(from_zero)
  
  
  graph = []
  ranks = {k: 0 for k in keys}
  parents = {k: k for k in keys}
  dist = []
  min_num_rolls = 0
  for i in range(len(keys) - 1):
    for j in range(i + 1, len(keys)):
      graph.append(Triad(keys[i], keys[j], get_num_rolls(keys[i], keys[j])))
  kruskal()
  # print([(x.source, x.target, x.weight) for x in dist])
  print(min_num_rolls + min_from_zero)




