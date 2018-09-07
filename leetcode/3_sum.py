# https://leetcode.com/problems/3sum/
def three_sum(nums):
  nums.sort()
  n = len(nums)
  result = []
  for i in range(n):
    if i > 0 and nums[i] == nums[i - 1]:
      continue
    target = nums[i] * (-1)
    s, e = i + 1, n - 1
    while s < e:
      if nums[s] + nums[e] == target:
        result.append([nums[i], nums[s], nums[e]])
        s += 1
        while s < e and nums[s] == nums[s - 1]:
          s += 1
      elif nums[s] + nums[e] < target:
        s = s + 1
      else:
        e = e - 1
  return result
print(three_sum([-1, 0, 1, 2, -1, -4]))
