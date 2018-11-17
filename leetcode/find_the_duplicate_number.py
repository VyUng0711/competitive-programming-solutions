# https://leetcode.com/problems/find-the-duplicate-number/description/

class Solution:
    # Time: O(n), Space: O(n) (not modifying the array)
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
            
    # Time: O(n log n), Space: O(n)
    def findDuplicate(self, nums):
        sorted_n = sorted(nums)
        for i in range(len(sorted_n) - 1):
            if sorted_n[i] == sorted_n[i + 1]:
                return sorted_n[i]
    
    # Time: O(n), Space: O(1)
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        i = nums[0]
        j = slow
        while i != j:
            i = nums[i]
            j = nums[j]
            
        return i
            
 
