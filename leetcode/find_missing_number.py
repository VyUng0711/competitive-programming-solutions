class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        real_n = n + 1
        real_sum = (n * (n + 1))//2
        missing_num = real_sum - sum(nums)

        return missing_num
        """
        :type nums: List[int]
        :rtype: int
        """
        