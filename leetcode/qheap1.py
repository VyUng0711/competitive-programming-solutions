# https://leetcode.com/problems/minimum-size-subarray-sum/description/
class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        
        curr_sum = 0
        min_len = len(nums) + 1
        
        start = 0
        end = 0
        
        while end < len(nums):
            while curr_sum < s and end < len(nums):
                curr_sum += nums[end]
                end += 1
            while curr_sum >= s and start < len(nums):
                if end - start < min_len:
                    min_len = end - start
                    
                # Advance start by 1
                curr_sum -= nums[start]
                start += 1
                
        if min_len > len(nums):
            return 0
        return min_len
