# Method 1:
import heapq

num_queries = int(input())
my_heap = []
deleted = {}
for i in range(num_queries):
  this_line = list(map(int, input().split()))
  if this_line[0] == 1:
    heapq.heappush(my_heap, this_line[1])
    if this_line[1] in deleted and deleted[this_line[1]] == True:
      deleted[this_line[1]] = False
  if this_line[0] == 2:
    deleted[this_line[1]] = True
  if this_line[0] == 3:
    min_element = my_heap[0]
    while min_element in deleted and deleted[min_element] == True:
      heapq.heappop(my_heap)
      min_element = my_heap[0]
    print (min_element)


# Method 2:
import queue
num_queries = int(input())
my_heap = queue.PriorityQueue()
deleted = {}
for i in range(num_queries):
  this_line = list(map(int, input().split()))
  if this_line[0] == 1:
    my_heap.put(this_line[1])
    deleted[this_line[1]] = False
  if this_line[0] == 2:
    deleted[this_line[1]] = True
  if this_line[0] == 3:
    min_element = my_heap.queue[0]
    while deleted.get(min_element, False) == True:
      my_heap.get()
      min_element = my_heap.queue[0]
    print (min_element)
  
    
  
    
    
  
    
    