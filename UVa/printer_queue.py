# UVA
# Complexity: O(n^2)
import queue
def printer_queue(arr, your_pos):
  pq = queue.PriorityQueue()
  q = queue.Queue()
  for x in arr:
    pq.put(-x)
    q.put(x)
  total_time = 0
  while True:
    while q.queue[0] < -pq.queue[0]:
      if your_pos == 0:
        your_pos = q.qsize() - 1
      else:
        your_pos -= 1
      e = q.get()
      q.put(e)
    q.get() #Complexity O(log n)
    pq.get()
    total_time += 1
    if your_pos == 0:
      break
    else:
      your_pos -= 1
  return total_time

num_tests = int(input())
for test in range(num_tests):
  n, m = map(int, input().split())
  priorities = list(map(int, input().split()))
  print(printer_queue(priorities, m))
