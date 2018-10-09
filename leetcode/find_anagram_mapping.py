# https://leetcode.com/problems/find-anagram-mappings/description/
class Solution:
    def anagramMappings(self, A, B):
        result = []
        map_b_value_to_index = {B[i]: i for i in range(len(B))}
        for i in range(len(A)):
            result.append(map_b_value_to_index[A[i]])
        return result
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
