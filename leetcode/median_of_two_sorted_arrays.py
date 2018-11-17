# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# Complexity O(m + n)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        def mergeSortedArrays(nums1, nums2):
            result = []
            i = 0
            j = 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    result.append(nums1[i])
                    i += 1
                else:
                    result.append(nums2[j])
                    j += 1
            while i < len(nums1):
                result.append(nums1[i])
                i += 1
            while j < len(nums2):
                result.append(nums2[j])
                j += 1
            return result
        merged = mergeSortedArrays(nums1, nums2)
        # print(merged)
        if len(merged) % 2 == 0:
            median = (merged[len(merged)//2 - 1] + merged[len(merged)//2])/2
        else:
            median = merged[len(merged)//2]
        return median

# Complexity O(log(r - l) * (log(n) + log(m))) 
# with r - l is the range of our binary search for the median
# Simple version:

import bisect
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        def find(k): 
            low = -10 ** 6
            high = 10 ** 6
            while low <= high:
                mid = (low + high) // 2

                left_a = bisect.bisect_right(nums1, mid)
                left_b = bisect.bisect_right(nums2, mid)

                if left_a + left_b >= k:
                    res = mid
                    high = mid - 1
                # return min(max(nums1[left_a - 1], nums2[left_b - 1]), median)
                else:
                    low = mid + 1
            return res

        N = len(nums1) + len(nums2)
        median = find((N + 1) // 2)
        if N % 2 == 1:
            return find(N // 2 + 1)
        else:
        # median2 = find((N + 1) // 2 + 1))
            return (find(N // 2) + find(N // 2 + 1)) / 2

# More complicated version:
import bisect
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
    
        if len(nums1) == 1 and len(nums2) == 1:
            return (nums1[0] + nums2[0]) / 2
            
        low = 0
        high = 10 ** 6
        if (len(nums1) + len(nums2)) % 2 == 0:
            avg = (len(nums1) + len(nums2)) // 2
        else:
            avg = ((len(nums1) + len(nums2)) // 2)+ 1
        
        while low <= high:
            median = (low + high) // 2
            print(low, median, high)
            
            left_a = bisect.bisect_right(nums1, median)
            left_b = bisect.bisect_right(nums2, median)
            print(left_a, left_b)
    
            if left_a + left_b == avg:
                print(left_a, left_b)
                max_left_a = float('-inf') if left_a == 0 else nums1[left_a - 1]
                min_right_a = float('inf') if left_a == len(nums1) else nums1[left_a]
                max_left_b = float('-inf') if left_b == 0 else nums2[left_b - 1]
                min_right_b = float('inf') if left_b == len(nums2) else nums2[left_b]
                
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return ((max(max_left_a, max_left_b) + min(min_right_a, min_right_b)) / 2)
                
                else:
                    return (max(max_left_a, max_left_b))
                
            elif left_a + left_b < avg:
                low = median + 1
            else:
                high = median - 1
        
        max_left_a = float('-inf') if left_a == 0 else nums1[left_a - 1]
        min_right_a = float('inf') if left_a == len(nums1) else nums1[left_a]
        max_left_b = float('-inf') if left_b == 0 else nums2[left_b - 1]
        min_right_b = float('inf') if left_b == len(nums2) else nums2[left_b]

        
        if left_a + left_b < avg:
            return min(min_right_a, min_right_b)
        else:
            return max(max_left_a, max_left_b)
# Complexity O(log(m + n))

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        def findMedian(small, large):
            
            small_len = len(small)
            large_len = len(large)
            
            low = 0
            high = small_len
            
            while low <= high: 
                partition_x = (low + high) // 2
                partition_y = ((small_len + large_len + 1) // 2 ) - partition_x
                max_left_x = float('-inf') if partition_x == 0 else small[partition_x - 1]
                min_right_x = float('inf') if partition_x == small_len else small[partition_x]
                max_left_y = float('-inf') if partition_y == 0 else large[partition_y - 1]
                min_right_y = float('inf') if partition_y == large_len else large[partition_y]

                
                if max_left_x <= min_right_y and max_left_y <= min_right_x:
                    if (small_len + large_len) % 2 == 0:
                        return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                    else:
                        return max(max_left_x, max_left_y)
                elif max_left_x > min_right_y:
                    high = partition_x - 1
                else:
                    low = partition_x + 1
            
        if len(nums1) <= len(nums2):
            return findMedian(nums1, nums2)
        else:
            return findMedian(nums2, nums1)
   


