import heapq

def add_all(a):
  costs = []
  last_sum = 0
  heapq.heapify(a)
  while len(a) > 0:
    if len(costs) == 0:
      first_num = heapq.heappop(a)
      second_num = heapq.heappop(a)
      last_sum = last_sum + first_num + second_num
    else:
      new_num = heapq.heappop(a)
      last_sum = last_sum + new_num
    costs.append(last_sum) 
  return (sum(costs))

# print (add_all([1,2,3]))
# print (add_all([1,2,3,4]))
while True:
  n = int(input())
  if n == 0:
    break
  array = list(map(int, input().split()))
  print (add_all(array))


