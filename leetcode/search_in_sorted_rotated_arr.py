# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# Recursion:
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def recurse_search(arr, low, high, key):
            if low > high: 
                return -1 
            mid = (low + high) // 2
            # If found key:
            if key == arr[mid]:
                return mid
            # If left side is sorted, then right side is not
            if arr[low] <= arr[mid]:
                # Check if key lies in left side:
                if key <= arr[mid] and key >= arr[low]:
                    return recurse_search(arr, low, mid - 1, key)
                # Else key lies in right side:
                return recurse_search(arr, mid + 1, high, key)
            # If left side is not sorted, then right side must be sorted
            else:
                # Check if key lies in right side:
                if key >= arr[mid] and key <= arr[high]:
                    return recurse_search(arr, mid + 1, high, key)
                # Else key lies in left side:
                return recurse_search(arr, low, mid - 1, key)
            
        return recurse_search(nums, 0, len(nums) - 1, target)

                
# Iterative:
class Solution:
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if nums[low] <= nums[mid]:
                if target <= nums[mid] and target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target <= nums[high] and target >= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

                
