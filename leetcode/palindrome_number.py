# https://leetcode.com/problems/palindrome-number/description/

# Complexity: O(log10 (n))
# Revert the entire number and compare
class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        k = x
        while k:
            digit = k % 10
            rev = rev * 10 + digit
            k = k // 10
        print(rev)
        if rev == x:
            return True
        return False

# Revert half the number and compare
class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x // 10
            print(x, rev)
        
        return x == rev or x == rev // 10

