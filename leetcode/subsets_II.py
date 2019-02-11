# https://leetcode.com/problems/subsets-ii/

import copy
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    # def get_subsets(nums)
        res = []
        nums = sorted(nums)
        def recurse(subset, indx):
            res.append(copy.deepcopy(subset))
            if indx == len(nums):
                return
            for i in range(indx, len(nums)):
                if i > indx and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                recurse(subset, i + 1)
                subset.pop()
        recurse([], 0)
        return res



