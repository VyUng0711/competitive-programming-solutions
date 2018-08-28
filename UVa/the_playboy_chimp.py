# UVA
# tallest one shorter and the shortest one taller
# ordered short -> tall

import bisect
n = int(input())
chimps = list(map(int, input().split()))
q = int(input())
queries = list(map(int, input().split()))

def binary_search(a, x):
  si = bisect.bisect_right(a, x, 0, n)
  if si <= n - 1:
    shortest = a[si]
  else:
    shortest = "X"
  
  ti = bisect.bisect_left(a, x, 0, n)
  if ti - 1 >= 0:
    tallest = a[ti - 1]
  else:
    tallest = "X"
      
  return tallest, shortest

for query in queries:
  tallest, shortest = binary_search(chimps, query)
  print(tallest, shortest)