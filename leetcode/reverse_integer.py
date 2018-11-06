# https://leetcode.com/problems/reverse-integer/description/
class Solution(object):
    def reverse(self, x):
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = x * sign
        res = 0
        while x:
            digit = x % 10
            res = res * 10 + digit
            x = x // 10
            # print (res)
        if -2 ** 31 <= res <= 2 ** 31:
            return res * sign
        return 0

