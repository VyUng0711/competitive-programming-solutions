# https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, A, B):
        def strStr(A, B):
            if A == "":
                if B == "":
                    return True
                return False
            if len(A) > len(B):
                return -1
            for i in range(len(B)):
                if B[i: i+len(A)] == A:
                    return True
            return False
        if len(A) == len(B):
            C = B + B
            return strStr(A, C)
        return False

        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        


