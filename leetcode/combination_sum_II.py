# https://leetcode.com/problems/combination-sum-ii/

import copy
class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates = sorted(candidates)
        def recurse(sub_a, sum_so_far, indx):
            # print('recurse({}, {}, {})'.format(sub_a, sum_so_far, indx))
            if sum_so_far > target:
                return
            if sum_so_far == target:
                sub_copy = copy.deepcopy(sub_a)
                res.append(sub_copy)
                return
            for i in range(indx, len(candidates)):
                if i > indx and candidates[i] == candidates[i - 1]:
                    continue
                sub_a.append(candidates[i])
                recurse(sub_a, sum_so_far + candidates[i], i + 1)
                sub_a.pop()
        recurse([], 0, 0)
        return res



