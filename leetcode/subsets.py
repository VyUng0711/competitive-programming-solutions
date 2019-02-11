# https://leetcode.com/problems/subsets/

# Backtracking:
import copy
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def recurse(subset, indx):
            if indx == len(nums):
                # print(subset)
                res.append(copy.deepcopy(subset))
                return
            recurse(subset, indx + 1)
            subset.append(nums[indx])
            recurse(subset, indx + 1)
            subset.pop()
        recurse([], 0)
        return res


# Another backtracking approach:
import copy
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def recurse(cur, index):
            print('recurse({}, {})'.format(cur, index))
            print(cur)
            res.append(copy.deepcopy(cur))
            if index == len(nums):
                return
                
            for i in range(index, len(nums)):
                cur.append(nums[i])
                recurse(cur, i + 1)
                cur.pop()
                index -= 1
        recurse([], 0)
        return res
