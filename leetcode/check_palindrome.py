class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)-1
        if len(s) == 0:
            return True
    
        while i < j:
            while not s[i].isalnum() and i < j:
                i+=1
            while not s[j].isalnum() and i < j:
                j-=1
            if s[i].lower() != s[j].lower():
                return False
            else:
                i = i+1
                j = j-1
        return True