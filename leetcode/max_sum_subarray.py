# https://leetcode.com/problems/maximum-subarray/description/
def maxSubArray(self, nums):
    global_max = nums[0]
    max_so_far = nums[0]
    for i in range(1, len(nums)):
        max_so_far = max(max_so_far + nums[i], nums[i])
        global_max = max(max_so_far, global_max)
    return global_max

#Same idea, but caching the results:
class Solution(object):
    def maxSubArray(self, nums):
        dp = [None] * len(nums)
        dp[0] = nums[0]
        global_max = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            global_max = max(global_max, dp[i])
        # print(dp)
        return global_max
