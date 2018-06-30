import queue
import heapq
import math

n = int(input())
# Want to return the first element of min_heap 
min_heap = []
max_heap = []
num_reviews = 0
for i in range(n):
  command = list(map(int, input().split()))
  if command[0] == 1:
    heapq.heappush(min_heap, command[1])
    heapq.heappush(max_heap, -heapq.heappop(min_heap))
    num_reviews += 1
    if len(min_heap) < math.floor(num_reviews/3):
      heapq.heappush(min_heap, -heapq.heappop(max_heap))
  else:
    if num_reviews > 2:
      print (min_heap[0])
    else:
      print ("No reviews yet")

      


