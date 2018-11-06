# https://leetcode.com/problems/powx-n/description/

# Fast power:
class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
      
        if n % 2 == 0:
            y = self.myPow(x, n // 2)
            return y * y
        else:
            return x * self.myPow(x, n - 1)

# Even fastter:
class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
      
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
