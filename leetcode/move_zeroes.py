# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums):
        i = 0 #index to put
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                     
