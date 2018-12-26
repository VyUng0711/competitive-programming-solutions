# https://leetcode.com/problems/license-key-formatting/

class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        count = 0
        S = S.replace('-','').upper()
        new_string = ''
        for i in range(len(S) - 1, -1, -1):
            new_string = S[i] + new_string
            count += 1
            if count == K and i != 0:
                new_string = '-' + new_string
                count = 0
        return new_string
            


