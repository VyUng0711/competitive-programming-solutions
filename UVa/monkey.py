# UVA
# def binary_search(dists, left, right):
#   res = 0
#   while left <= right:
#     mid = (left + right) // 2
#     k = mid
#     for d in dists:
#       if d > k:
#         k = -1
#         break
#       elif d == k:
#         if k < 0:
#           break
#         k -= 1
#       else:
#         continue
#     # print(mid)
#     if k >= 0:
#       res = mid
#       right = mid - 1
#     else:
#       left = mid + 1
#   return res



def get_distances(rs):
  dists = []
  for i in range(len(rs)):
    if i == 0:
      dists.append(rs[i])
    else:
      dists.append(rs[i] - rs[i - 1])
  return dists

def binary_search(dists, left, right):
  while left <= right:
    mid = (left + right) // 2
    k = mid
    for d in dists:
      if d > k:
        k = -1
        break
      elif d == k:
        if k < 0:
          break
        k -= 1
      else:
        continue
    # print(mid)
    if k == 0:
      return mid
    elif k > 0:
      right = mid - 1
    else:
      left = mid + 1
  return left



num_tests = int(input())
for t in range(num_tests):
  n = int(input())
  rs = list(map(int, input().split()))
  dists = get_distances(rs)
  # print(dists)
  result = binary_search(dists, 0, 10**7)
  print("Case {}: {}".format(t + 1, result ))