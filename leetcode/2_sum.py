# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums, target):
        d = dict()
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            d[nums[i]] = i
