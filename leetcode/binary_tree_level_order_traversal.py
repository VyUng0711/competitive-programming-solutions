# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def levelOrder(self, root):
        if root == None:
            return []
        q = queue.Queue()
        q.put(root)
        result = []
        while not q.empty():
            level_size = q.qsize()
            this_level = []
            for i in range(level_size):
                top = q.get()
                if top.left:
                    q.put(top.left)
                if top.right:
                    q.put(top.right)
                this_level.append(top.val)
            result.append(this_level)
        return result
                
    # Another solution using dictionary
    def levelOrder(self, root):
        if root == None:
            return []
        results = {}
        visited = set()
        q = queue.Queue()
        q.put((root, 0))
        while not q.empty():
            top, level = q.get()
            if level in results:
                results[level].append(top.val)
            else:
                results[level] = []
                results[level].append(top.val)
            if top.left:
                q.put((top.left, level + 1))
                
            if top.right:
                q.put((top.right, level + 1))
        out = [x for x in results.values()]
        return out
                
        
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
