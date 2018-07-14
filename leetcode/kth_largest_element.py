import heapq

def kth_largest_element(nums, k):
	heapq.heapify(nums)
	for _ in range(len(nums) - k):
		heapq.heappop(nums)
	return nums[0]

def kth_largest_element_1(nums, k):
  min_heap = []
  max_heap = []
  for num in nums:
    heapq.heappush(min_heap, num)
    if len(min_heap) > k:
      heapq.heappush(max_heap, heapq.heappop(min_heap))
#   print(min_heap)
#   print(max_heap)
  return(min_heap[0])

kth_largest_element([3,2,3,1,2,4,5,5,6], 4)