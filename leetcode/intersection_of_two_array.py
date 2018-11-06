# https://leetcode.com/problems/intersection-of-two-arrays/description/

class Solution:
    def intersection(self, nums1, nums2):
        dict_1 = set()
        for i in nums1:
            dict_1.add(i)
            
        dict_2 = set()
        for j in nums2:
            dict_2.add(j)

        result = set()
        for k in dict_1:
            if k in dict_2:
                result.add(k)
        return list(result)



