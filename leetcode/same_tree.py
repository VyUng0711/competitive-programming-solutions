# https://leetcode.com/problems/same-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution using stack:
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
     
        def dfs(s):
            stack = []
            result = []
            stack.append(s)
            while len(stack) > 0:
                cur = stack.pop()
                if not cur:
                    result.append(None)
                else:
                    result.append(cur.val)
                    stack.append(cur.right)
                    stack.append(cur.left)
            return result
        pr = dfs(p)
        qr = dfs(q)
        if len(pr) != len(qr):
            return False
        for i in range(len(pr)):
            if pr[i] != qr[i]:
                return False
        return True
            
            
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

# Recursive Solution:
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        if p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False
