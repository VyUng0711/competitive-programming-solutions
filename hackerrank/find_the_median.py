import heapq
n = int(input())
a = list(map(int, input().split()))


def findMedian(arr):
  sorted_arr = sorted(arr)
  return sorted_arr[len(arr)//2]

def findMedian_1(arr):
  heapq.heapify(arr)
  for i in range(len(arr)//2):
    heapq.heappop(arr)
  return arr[0]
print(findMedian(a))