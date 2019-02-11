# https://leetcode.com/problems/permutations/

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def permutation(nums, l, r):
            if l == r:
                res.append(nums)
            else:
                for i in range(l, len(nums)):
                    new_nums = copy.deepcopy(nums)
                    new_nums[l], new_nums[i] = new_nums[i], new_nums[l]
                    permutation(new_nums, l + 1, r)
        permutation(nums, 0, len(nums) - 1)
        return res
                


