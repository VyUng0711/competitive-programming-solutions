# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # Method 1: Recursion:
    def invertTree(self, root):
        if not root:
            return None
        right = root.right
        left = root.left
        root.right = self.invertTree(left)
        root.left = self.invertTree(right)
        return root

    # Method 2: Iterative
    def invertTree(self, root):
        q = queue.Queue()
        q.put(root)
        if not root:
            return None 
        while not q.empty():
            top = q.get()
            temp = top.left
            top.left = top.right
            top.right = temp
            if top.left:
                q.put(top.left)
            if top.right:
                q.put(top.right)
            
        return root
    
