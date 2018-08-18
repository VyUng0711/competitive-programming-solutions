INF = float('inf')

#METHOD 1:
def floyd_warshall():
  for k in range(49):
    for i in range(49):
      for j in range(49):
        if dist[i][k] + dist[k][j] > dist[i][j]:
          dist[i][j] = dist[i][k] + dist[k][j]
    
        
num_tests = int(input())
for t in range(num_tests):
  num_orders = int(input())
  dist = [[0 if i <= j else -INF for j in range(49)] for i in range(49)]
  
  last_time = 0
  for o in range(num_orders):
    s, e, c = map(int, input().split())
    dist[s][e] = max(c, dist[s][e])
    

  floyd_warshall()
  print (dist[0][48])



# #METHOD 2:
# def dynamic_programming():
#   best_comp_so_far = [0] * (last_time + 1)
  
#   for j in range(1, last_time + 1):
#     for i in range(j):
#       temp_comp = best_comp_so_far[i] + dist[i][j]
#       if temp_comp > best_comp_so_far[j]:
#         best_comp_so_far[j] = temp_comp
#   return best_comp_so_far[last_time]          


# num_tests = int(input())
# for t in range(num_tests):
#   num_orders = int(input())
  
#   dist = [[0 for i in range(49)] for j in range(49)]
#   last_time = 0
#   for o in range(num_orders):
#     s, e, c = map(int, input().split())
#     dist[s][e] = max(dist[s][e], c)
#     if e > last_time:
#       last_time = e
#   result = dynamic_programming()
#   print(result)
#   