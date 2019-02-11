# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack_s = []
        stack_t = []
        for i in S:
            if i != "#":
                stack_s += i
            else:
                if stack_s:
                    stack_s.pop()
        for j in T:
            if j != "#":
                stack_t += j
            else:
                if stack_t:
                    stack_t.pop()
        if len(stack_s) != len(stack_t):
            return False
        for k in range(len(stack_s)):
            if stack_s[k] != stack_t[k]:
                return False
        return True


