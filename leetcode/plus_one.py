# https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits):
        result = []
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                this_col = digits[i] + 1 + carry
            else:
                this_col = digits[i] + carry
            
            if this_col < 10:
                result = [this_col] + result
                carry = 0
        
            else:
                if i == 0:
                    result = [1, 0] + result
                else:
                    result = [0] + result
                    carry = 1
            print(carry)
        return result
            
            
        """
        :type digits: List[int]
        :rtype: List[int]
        """
