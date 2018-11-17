# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        INF = float('-inf')
        def get_height(root, height):
            if not root:
                return 0
            left = get_height(root.left, height + 1)
            if left == INF:
                return INF
            right = get_height(root.right, height + 1) 
            if right == INF:
                return INF
            if abs(left - right) > 1:
                return INF
            return 1 + max(left, right)
        
        return get_height(root, 0) != INF
        
