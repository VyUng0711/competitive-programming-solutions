# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) - 1
        j = len(num2) - 1
        res = []
        carry = 0
        while i >= 0 or j >= 0:
            if i >= 0:
                a = int(num1[i])
            else:
                a = 0
            if j >= 0:
                b = int(num2[j])
            else:
                b = 0
            r = a + b + carry
            carry = r // 10
            res.append(str(r % 10))
            i -= 1
            j -= 1
        if carry > 0:
            res.append(str(carry))
        f = []
        for i in range(len(res) - 1, -1, -1):
            f.append(res[i])
        return (''.join(f))
            
        
        

