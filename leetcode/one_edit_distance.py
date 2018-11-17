# https://leetcode.com/problems/one-edit-distance/

# Shorter approach:
class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def isOneReplaceDistance(s, t):
            found = False
            for i in range(len(s)):
                if s[i] != t[i]:
                    if found:
                        return False
                    found = True
            return found
        def isOneInsertDistance(short, long):
            i = 0
            j = 0
            while i < len(short) and j < len(long):
                if short[i] != long[j]:
                    if i != j:
                        return False
                    j += 1
                else:
                    i += 1
                    j += 1
                    
            return True
                        
        if len(s) == len(t):
            return isOneReplaceDistance(s, t)
        elif len(s) - len(t) == 1:
            return isOneInsertDistance(t, s)
        elif len(t) - len(s) == 1:
            return isOneInsertDistance(s, t)
        return False
        
# Longer approach:

class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def isOneReplaceDistance(s, t):
            found = False
            for i in range(len(s)):
                if s[i] != t[i]:
                    if found:
                        return False
                    found = True
            return found
        
        def isOneInsertDistance(short, long):
            i = 0
            j = 0
            found = False
            while i < len(short) and j < len(long):
                if short[i] != long[j]:
                    if found:
                        return False
                    found = True
                    j += 1
                else:
                    i += 1
                    j += 1
            if j == len(long) - 1:
                if found:
                    return False
                else:
                    return True
            return found
                        
        if len(s) == len(t):
            return isOneReplaceDistance(s, t)
        elif len(s) < len(t):
            return isOneInsertDistance(s, t)
        else:
            return isOneInsertDistance(t, s)
                    


