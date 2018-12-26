# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = []
        top = None
        for i in range(numRows):
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1, 1])
                top = [1, 1]
            else:
                new = []
                new.append(1)
                for j in range(len(top) - 1):
                    new.append(top[j] + top[j + 1])
                new.append(1)
                res.append(new)
                top = new
        return res


