# https://leetcode.com/problems/implement-strstr/
# Solution with string slicing:
def strStr(self, haystack, needle):
    if needle == "":
        return 0
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack)):
        if haystack[i: i+len(needle)] == needle:
            return i 
    return -1

# Solution with no string slicing:
def strStr(self, haystack, needle):
    if needle == "":
        return 0
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            j = i + 1
            k = 1
            while j < len(haystack) and k < len(needle):
                if haystack[j] == needle[k] and k == len(needle) - 1: 
                    return (i)
                if haystack[j] != needle[k]:
                    break
                else:
                    j += 1
                    k += 1 
            if k == len(needle):
                return i      
    return -1
                    
# Solution using Knuth-Morris-Pratt Algorithm:
class Solution:
    def KMPPreprocess(self, p, kmp):
        m = len(p)
        kmp[0] = 0
        i = 1
        j = 0
        while i < m:
            if p[i] == p[j]:
                j += 1
                kmp[i] = j
                i += 1
            else:
                if j != 0:
                    j = kmp[j - 1]
                else:
                    kmp[i] = 0
                    i += 1
                    
    def KMPSearch(self, t, p, kmp):
        m = len(p)
        n = len(t)
        i = 0
        j = 0
        while i < n:
            if p[j] == t[i]:
                i += 1
                j += 1
            if j == m:
                # print("Found pattern at index {}".format(i - j))
                return (i - j)
                # j = kmp[j - 1]
            elif i < n and p[j] != t[i]:
                if j != 0:
                    j = kmp[j - 1]
                else:
                    i += 1
        return -1
        
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            return -1
        kmp = [None] * len(needle)
        self.KMPPreprocess(needle, kmp)
        return self.KMPSearch(haystack, needle, kmp)        
        
