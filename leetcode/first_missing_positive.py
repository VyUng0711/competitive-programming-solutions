# https://leetcode.com/problems/first-missing-positive/

# O(n) time, O(n) space
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = set()
        for num in nums:
            if num > 0:
                unique.add(num)
        
        for i in range(len(unique) + 1):
            if i + 1 not in unique:
                return i + 1 

# O(n) time, O(1) space: 


