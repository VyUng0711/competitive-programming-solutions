def subarraySum(nums, k):
  n = len(nums)
  sum_dict = {}
  sum_dict[0] = 1
  cur_sum = 0
  count = 0
  for num in nums:
    cur_sum += num
    if cur_sum - k in sum_dict.keys():
      count += sum_dict[cur_sum - k]
    sum_dict[cur_sum] = sum_dict.get(cur_sum, 0) + 1
  return count
print(subarraySum([3,4,7,2,-3,1,4,2],7))
     
    

def subarraySum1(nums, k):
  n = len(nums)
  count = 0
  for i in range(n):
    cur_sum = 0
    for j in range(i, n):
      cur_sum = cur_sum + nums[j]
      if cur_sum == k:
        count += 1
  return count


def subarraySum2(nums, k):
  dict_sum = {}
  n = len(nums)
  cur_sum = 0
  count = 0
  for i in range(0, n):
    cur_sum += nums[i]
    dict_sum[(0,i)] = cur_sum
  for j in range(1, n):
    for h in range(j, n):
      dict_sum[(j, h)] = dict_sum[(0, h)] - dict_sum[(0, j-1)]
  for v in (dict_sum.values()):
    if v == k:
      count += 1
  return count
    