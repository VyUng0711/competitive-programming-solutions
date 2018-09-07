# https://leetcode.com/problems/merge-sorted-array/description/
# Best runtime
def merge(nums1, nums2, m, n):
  if n == 0:
    pass
  else:
    nums1[m:] = nums2[:n]
    for ind, num in enumerate(sorted(nums1)):
      nums1[ind] = num
  # print(nums1)

# Medium runtime
def merge(nums1, nums2, m, n):
  j = m - 1
  curr_fill = len(nums1) - 1
  for i in range(n - 1, -1, -1):
    while j >= 0 and nums2[i] < nums1[j]:
      nums1[curr_fill] = nums1[j]
      j -= 1
      curr_fill -= 1
    nums1[curr_fill] = nums2[i]
    curr_fill -= 1
  # print(nums1)

# Worst runtime
def merge(nums1, nums2, m, n):
  k = m + n - 1
  i = m - 1
  j = n - 1
  while i >= 0 and j >= 0:
    if nums2[j] > nums1[i]:
      nums1[k] = nums2[j]
      j -= 1
      k -= 1
    else:
      nums1[k] = nums1[i]
      i -= 1
      k -= 1
  if j >= 0:
    nums1[:j+1] = nums2[:j+1]
    
