
# https://leetcode.com/problems/divide-two-integers/description/
# Not using bitwise operator:
class Solution(object):
    def divide(self, dividend, divisor):
        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        q = 0
        while dividend >= divisor:
            q += 1
            dividend -= divisor
        return sign * q 



