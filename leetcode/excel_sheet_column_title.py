# https://leetcode.com/problems/excel-sheet-column-title/description/

class Solution:
    def convertToTitle(self, n):
        
        r = ''
        while (n > 0):
            n -= 1
            r = chr(n % 26 + 65) + r
            n = n // 26
        return r
