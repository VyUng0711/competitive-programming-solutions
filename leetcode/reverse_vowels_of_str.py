# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution:
    def reverseVowels(self, s):
        vowels = {'o', 'e', 'i', 'a', 'u', 'O', 'E', 'I', 'A', 'U'}
        s_list = list(s)
        j = len(s) - 1
        i = 0
        while i < j:
            if s_list[i] in vowels and s_list[j] in vowels:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1
            elif s_list[i] in vowels:
                j -= 1
            elif s_list[j] in vowels:
                
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(s_list)
        """
        :type s: str
        :rtype: str
        """
