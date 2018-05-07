#26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        cur_num = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == cur_num:
                nums.remove(nums[i])
            else:
                cur_num = nums[i]
                i+=1
        return len(nums)