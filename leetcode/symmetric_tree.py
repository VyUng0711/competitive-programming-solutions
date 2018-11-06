# https://leetcode.com/problems/symmetric-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative approach:
import queue

class Solution(object):
    def isSymmetric(self, root):
        start = root
        q = queue.Queue()
        q.put(start)
        q.put(start)
        while not q.empty():
            first = q.get()
            second = q.get()
            if not first and not second:
                continue
            elif not first or not second:
                return False
            elif first.val != second.val:
                return False
            q.put(first.left)
            q.put(second.right)
            q.put(first.right)
            q.put(second.left)
            
        return True

# Recursive approach
class Solution(object):
    def isSymmetric(self, root):
        def compare(x, y):
            if not x and not y:
                return True
            if not x or not y:
                return False
            return x.val == y.val and compare(x.left, y.right) and compare(x.right, y.left)

        if not root:
            return True
        return compare(root.left, root.right)



