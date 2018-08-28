# https://leetcode.com/problems/sliding-window-maximum/description/
from collections import deque
def sliding_window_maximum(arr, k):
  n = len(arr)
  dq = deque()
  result = []
  for i in range(k):
    while dq and arr[i] >= arr[dq[-1]]:
      dq.pop()
    dq.append(i)
  for i in range(k, n):
    result.append(arr[dq[0]])
    while dq and dq[0] <= i - k:
      dq.popleft()
    while dq and arr[i] >= arr[dq[-1]]:
      dq.pop()
    dq.append(i)
  result.append(arr[dq[0]])
  return result
print(sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3))
    
    
