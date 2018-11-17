# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums):
        if nums[-1] >= nums[0]:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            # If left array is sorted, find in right array
            if nums[left] < nums[mid]:
                left = mid + 1
            # If left array is not sorted, find in left array
            else:
                right = mid - 1
                

