# https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/monk-and-multiplication/
import queue 
n = int(input())
array = list(map(int, input().split()))
def monk_and_multiplication(a):
  negative = [-x for x in a]
  #print (negative)
  q = queue.PriorityQueue()
  products = []
  for i in range(len(a)):
    q.put(negative[i])
    if i < 2:
      products.append(-1) 
    else:
      smallest = q.get()
      second_smallest = q.get()
      third_smallest = q.get()
      product = -smallest * second_smallest * third_smallest
      q.put(smallest)
      q.put(second_smallest)
      q.put(third_smallest)
      products.append(product)
  return products  

def monk_and_multiplication2(a):
  q = queue.PriorityQueue()
  products = []
  for i in range(len(a)):
    q.put(a[i])
    if i < 2:
      products.append(-1)
    else:
      if q.qsize() > 3:
        q.get()
      product = q.queue[0] * q.queue[1] * q.queue[2]
      products.append(product)
      
  return products 

print (*monk_and_multiplication2(array), sep = '\n')
      

      
    
  