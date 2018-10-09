# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
 
# Case 1: If two arrays were not sorted and have comparable size
class Solution:
    def intersect(self, nums1, nums2):
        dict_1 = dict()
        for i in nums1:
            dict_1[i] = dict_1.get(i, 0) + 1
        dict_2 = dict()
        for j in nums2:
            dict_2[j] = dict_2.get(j, 0) + 1
        
        result = []
        for k, v in dict_1.items():
            if k in dict_2:
                fre = min(v, dict_2[k])
                for f in range(fre):
                    result.append(k)
        return reversed
    
# Case 2: If two arrays were sorted, use 2 pointers
class Solution:
    def intersect(self, nums1, nums2):
        i = 0
        j = 0
        # nums1.sort()
        # nums2.sort()
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        return result

#   If two arrays were sorted
#     def intersect(self, nums1, nums2):
#         j = 0
#         result = []
#         for i in range(len(nums1)):
#             if j == len(nums2):
#                 break
                
#             if nums1[i] < nums2[j]:
#                 continue
#             elif nums1[i] > nums2[j]:
#                 j += 1
#             else:
#                 result.append(nums1[i])
#                 j += 1
#         return result


# Case 3: If one array is significantly shorter than the other.
    
class Solution:
    def intersect(self, nums1, nums2):
        small_dict = dict()
        if len(nums1) <= len(nums2):
            for i in nums1:
                small_dict[i] = small_dict.get(i, 0) + 1
            long_dict = nums2
            
        elif len(nums1) > len(nums2):
            for j in nums2:
                small_dict[j] = small_dict.get(j, 0) + 1
            long_dict = nums1
        
        result = []
        for item in long_dict:
            if item in small_dict:
                if small_dict[item] > 0: 
                    result.append(item)
                    small_dict[item] -= 1

        return result  


    

        
