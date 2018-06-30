import queue

def guess_data_structure(queries):
  s = []
  q = queue.Queue()
  h = queue.PriorityQueue()
  is_stack = True
  is_queue = True
  is_priority_queue = True
  for query in queries:
    if query[0] == 1:
      if is_stack:
        s.append(query[1])
      if is_queue:
        q.put(query[1])
      if is_priority_queue:
        h.put(-query[1])
    else:
      if is_stack:
        if len(s) == 0 or query[1] != s[-1]:
          is_stack = False
        else:
          s.pop()
      if is_queue:
        if q.empty() or query[1] != q.queue[0]:
          is_queue = False
        else:
          q.get()
      if is_priority_queue:
        if h.empty() or -query[1] != h.queue[0]:
          is_priority_queue = False
        else:
          h.get()
          
  if is_stack and not is_queue and not is_priority_queue:
    return ("stack")
  if is_queue and not is_stack and not is_priority_queue:
    return ("queue")
  if is_priority_queue and not is_stack and not is_queue:
    return ("priority queue")
  if not is_stack and not is_queue and not is_priority_queue:
    return ("impossible")
  else:
    return ("not sure")

        

while True: 
  n = int(input())
  if n == "":
    break
  queries = []
  for i in range(n):
    command, element = map(int, input().split())
    queries.append((command, element))
  print (guess_data_structure(queries))
      
      
      
    
