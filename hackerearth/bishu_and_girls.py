import operator
n = int(input())
graph = [[] for i in range(n)]
for i in range(n - 1):
  #print(input())
  #continue
  u, v = map(int, input().split())
  graph[u-1].append(v-1)
  graph[v-1].append(u-1)
#exit()
  
q = int(input())
girls = []
for j in range(q):
  value = int(input())
  girls.append(value-1)
  
#print (girls)

distances = {}
visited = [False]*n
path = [-1]*n

def DFS(source):
  s = []
  visited[source] = True
  s.append(source)
  distances[source] = 0
  while len(s) > 0:
    u = s[-1]
    s.pop()
    for v in graph[u]:
      if visited[v] == False:
        s.append(v)
        visited[v] = True
        path[v] = u
        distances[v] = distances[u]+1



# def calculate_distance(s, f):
#   distance = 0
#   if f == s:
#     return 0
#   if path[f] == -1:
#     return -1
#   while True:
#     distance += 1
#     f = path[f]
#     if f == s:
# #      distance +=1
#       break
#   return distance

# O(n)
DFS(0)
#print (distances)
min_dist = n - 1
min_id = None
for key in girls:
  if distances[key] < min_dist or (distances[key] == min_dist and min_id > key):
    min_dist = distances[key]
    min_id = key

print (min_id + 1)   
  

# O(q * n)

# for g in girls:
#   this_dist = calculate_distance(0, g)
#   distances[g] = this_dist
#print (distances)

# index = min(girls_dists, key=girls_dists.get)
# print (index + 1)

# 
#   
# 
#   
