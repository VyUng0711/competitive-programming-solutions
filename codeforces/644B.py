import queue
def processing_queries(n,b,q):
  result=[]
  finished=q[0][0]+q[0][1]
  result.append(finished)
  queries=queue.Queue()
  queries.put(finished)
  for i in range(1,len(q)):
    while queries.qsize() > 0 and q[i][0] >= queries.queue[0]:
      queries.get()
    if finished <= q[i][0]:
      finished=q[i][0]+q[i][1]
      result.append(finished)
      queries.put(finished)
    else:
      if queries.qsize() > b:
        result.append(-1)
      else:
        finished+=q[i][1]
        result.append(finished)
        queries.put(finished)
  print (*result)
  
n,b=[int(x) for x in input().split()]
list_of_queries=[]
for i in range(n):
  this_q=[int(x) for x in input().split()]
  list_of_queries.append(this_q)
#processing_queries(5,1,[[2,9],[4,8],[10,9],[15,2],[19,1]])
processing_queries(n,b,list_of_queries)