# https://leetcode.com/problems/combinations/

import copy
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def recurse(cur, indx, l):
            # print('recurse({}, {}, {})'.format(cur, indx, l))
            if l == k:
                res.append(copy.deepcopy(cur))
                return
            else:
                for i in range(indx, n + 1):
                    cur.append(i)
                    recurse(cur, i + 1, l + 1)
                    cur.pop()
        recurse([], 1, 0)
        return res
        
