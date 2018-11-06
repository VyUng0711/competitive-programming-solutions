# https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def __init__(self):
    #     self.result = []
    def binaryTreePaths(self, root):
        res = []
        path = ''
        self.dfs(root, path, res)
        return res
        # stack = []
        # stack.append(root)
        # while len(stack) > 0:
        #     cur = stack.pop()
        #     if not cur:
        #         result.append()
    def dfs(self, root, path, res):
        if not root:
            return res
        if root:
            path = path + str(root.val) + '->'
            if not root.left and not root.right:
                res.append(path[:-2])
            else:
                if root.left:
                    self.dfs(root.left, path, res)
                if root.right:
                    self.dfs(root.right, path, res)
