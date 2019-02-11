# https://leetcode.com/problems/letter-case-permutation/
# Using backtracking:
import copy
class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        def recurse(cur, indx):
            if len(cur) == len(S):
                res.append(''.join(cur))
            if indx == len(S):
                return
            else:
                if S[indx].isalpha():
                    cur.append(S[indx].lower())
                    recurse(cur, indx + 1)
                    cur.pop()
                    cur.append(S[indx].upper())
                    recurse(cur, indx + 1)
                    cur.pop()
                else:
                    cur.append(S[indx])
                    recurse(cur, indx + 1)
                    cur.pop()
        recurse([], 0)
        return res

# Using simple recursion:

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        def recurse(cur, indx):
            if len(cur) == len(S):
                res.append(''.join(cur))
            
            if indx == len(S):
                return
            else:
                if S[indx].isalpha():
                    recurse(cur + S[indx].lower(), indx + 1)
                    recurse(cur + S[indx].upper(), indx + 1)
                else:
                    recurse(cur + S[indx], indx + 1)
    
        recurse("", 0)
        return res
                
                
            
   
                
                
            
        


