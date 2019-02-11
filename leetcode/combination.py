# https://leetcode.com/problems/combination-sum/

import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def recurse(sub_a, sum_so_far, indx):
            # print('recurse({}, {}, {})'.format(sub_a, sum_so_far, indx))
            if sum_so_far > target:
                return
            if sum_so_far == target:
                sub_copy = copy.deepcopy(sub_a)
                res.append(sub_copy)
                return
            for i in range(indx, len(candidates)):
                sub_a.append(candidates[i])
                recurse(sub_a, sum_so_far + candidates[i], i)
                sub_a.pop()
        recurse([], 0, 0)
        return res



