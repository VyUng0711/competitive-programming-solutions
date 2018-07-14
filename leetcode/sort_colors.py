def sort_colors(nums):
  end_of_0 = 0
  end_of_2 = len(nums) - 1
  i = 0
  while i < end_of_2:
    if nums[i] == 0:
      nums[end_of_0], nums[i] = nums[i], nums[end_of_0]
      end_of_0 += 1
    elif nums[i] == 2:
      nums[end_of_2], nums[i] = nums[i], nums[end_of_2]
      end_of_2 -= 1
      i -= 1
    i += 1
  print(nums)
  
  
def sort_colors1(nums):
  dict_count = {}
  for i in nums:
    dict_count[i] = dict_count.get(i,0) + 1
  index = 0
  for key, value in dict_count.items():
    for j in range(value):
      nums[index] = key
      index += 1
sort_colors([2,0,2,1,1,0])