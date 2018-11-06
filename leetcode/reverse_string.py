class Solution:
    def reverseString(self, s):
        # return s[::-1]
        res = ""
        for i in range(len(s) - 1, -1, -1):
            res += s[i]
        return res
