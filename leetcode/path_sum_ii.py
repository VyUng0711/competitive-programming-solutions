# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        
        def recurse(root, sum, history, result):
            if not root:
                return
            
            history.append(root.val)
            
            if not root.left and not root.right and root.val == sum:
                cur = [x for x in history]
                result.append(cur)
                
            recurse(root.left, sum - root.val, history, result)
            recurse(root.right, sum - root.val, history, result)
            
            history.pop()
            
        result = []
        cur_res = []
        recurse(root, sum, cur_res, result)
        return result
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
   

