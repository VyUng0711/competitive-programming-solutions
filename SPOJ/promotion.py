import heapq
n = int(input())
min_heap = []
max_heap = []
dict = {}
total = 0
for i in range(n):
  this_day = list(map(int, input().split()))
  k = this_day[0]
  bills = this_day[1:]
  for bill in bills:
    heapq.heappush(min_heap, bill)
    heapq.heappush(max_heap, -bill)
    dict[bill] = dict.get(bill, 0) + 1
  while True:
    get_max = -max_heap[0]
    if dict[get_max] > 0:
      max_value = -heapq.heappop(max_heap)
      dict[max_value] -= 1
      break
    heapq.heappop(max_heap)
  while True:
    get_min = min_heap[0]
    if dict[get_min] > 0:
      min_value = heapq.heappop(min_heap)
      dict[min_value] -= 1
      break
    heapq.heappop(min_heap)
  prize = max_value - min_value
  total += prize
print (total)