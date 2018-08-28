# https://www.spoj.com/problems/EKO/
num_trees, wood_amount = map(int, input().split())
heights = list(map(int, input().split()))


# 0 --> a[num_trees - 1]
def binary_search(heights, left, right):
  while left <= right:
    mid = (left + right) // 2
    cut = 0
    for h in heights:
      cut += max(0, h - mid)
    # print(cut)
    if cut == wood_amount:
      return mid
    elif cut > wood_amount:
      left = mid + 1
    else:
      right = mid - 1
  return right
      
heights.sort()
# print(heights)
print(binary_search(heights, 0, heights[-1]))
