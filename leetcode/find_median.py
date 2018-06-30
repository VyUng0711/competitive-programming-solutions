import heapq


def get_median_1(sequence):
  min_heap = []
  max_heap = []
  medians = []
  for i in sequence:
    heapq.heappush(max_heap, -heapq.heappushpop(min_heap, i))
    if len(max_heap) > len(min_heap):
      heapq.heappush(min_heap, -heapq.heappop(max_heap))
    if len(max_heap) == len(min_heap):
      medians.append((min_heap[0] + (-max_heap[0]))/2)
    else:
      medians.append(min_heap[0])
  return medians
      
def get_median_2(sequence):
  min_heap = []
  max_heap = []
  medians = []
  for i in sequence:
    if len(min_heap) == len(max_heap):
      heapq.heappush(min_heap, i)
      if len(min_heap) >=1 and len(max_heap) >=1 and min_heap[0] < -max_heap[0]:
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
      medians.append(min_heap[0])
    else:
      heapq.heappush(max_heap, -i)
      if len(min_heap) >=1 and len(max_heap) >=1 and min_heap[0] < -max_heap[0]:
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
      medians.append((min_heap[0] - max_heap[0])/2)
    print (min_heap, max_heap)
  return medians


s = list(map(int, input().split()))
print(get_median_1(s))
         