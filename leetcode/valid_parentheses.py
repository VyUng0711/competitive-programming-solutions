# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s):
        pair = {'(': ')', '{': '}', '[' : ']'}
        stack = []
        for i in range(len(s)):
            if s[i] in pair:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                else:
                    if pair[stack[-1]] == s[i]:
                        stack.pop()
                    else:
                        return False
        return not stack


