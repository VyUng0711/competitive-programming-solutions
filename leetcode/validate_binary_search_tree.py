# https://leetcode.com/problems/validate-binary-search-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Method 1: Do an inorder traversal
# and compare newly checked node with recently added node 
class Solution:
    def __init__(self):
        # self.traversal_result = []
        self.recently_added = float('-inf')
        self.result = True
        
    def inorder_traversal(self, root):
        if not root:
            return False
        self.inorder_traversal(root.left)
        if root.val <= self.recently_added:
            self.result = False
            return
        # self.traversal_result.append(root.val)
        self.recently_added = root.val
        self.inorder_traversal(root.right)
        
    def isValidBST(self, root):
        result = []
        self.inorder_traversal(root)
        if not self.result:
            return False
        return True
        
        """
        :type root: TreeNode
        :rtype: bool
        """

# Method 2: Use recursion

class Solution:
    def isValidBST(self, root, min_val = float('-inf'), max_val = float('inf')):
        if not root:
            return True
        validate_root = (min_val <= root.val < max_val)
        validate_left = self.isValidBST(root.left, min_val, root.val)
        validate_right = self.isValidBST(root.right, root.val + 1, max_val)
        return validate_root and validate_left and validate_right
            
        """
        :type root: TreeNode
        :rtype: bool
        """
