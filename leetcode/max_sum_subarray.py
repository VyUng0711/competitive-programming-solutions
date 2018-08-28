# https://leetcode.com/problems/maximum-subarray/description/
def maxSubArray(self, nums):
    global_max = nums[0]
    max_so_far = nums[0]
    for i in range(1, len(nums)):
        max_so_far = max(max_so_far + nums[i], nums[i])
        global_max = max(max_so_far, global_max)
    return global_max