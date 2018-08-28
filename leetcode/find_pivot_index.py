# https://leetcode.com/problems/find-pivot-index/
def find_pivot_index(nums):
  nums_sum = 0
  left_sum = 0
  for num in nums:
    nums_sum += num
  for i in range(len(nums)):
    if left_sum == nums_sum - left_sum - nums[i]:
      return i
    left_sum += nums[i]
  return -1
    
      
print(find_pivot_index([1,7,3,6,5,6]))
print(find_pivot_index([-1,-1,0,-1,-1,0]))   
print(find_pivot_index([-1,-1,-1,-1,-1,0]))