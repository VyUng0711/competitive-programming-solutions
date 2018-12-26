# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        # self.length = 0
        self.left = None
        self.right = None
# Using DFS:
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [(root, sum - root.val)]
        while stack:
            top, cur_sum = stack.pop()
            if not top.left and not top.right:
                if cur_sum == 0:
                    return True
            else:
                if top.left:
                    stack.append((top.left, cur_sum - top.left.val))
                if top.right:
                    stack.append((top.right, cur_sum - top.right.val))
        return False


# Using BFS:
from queue import Queue
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        q = Queue()
        q.put(root)
        while not q.empty():
            top = q.get()
            if not top.left and not top.right:
                if top.val == sum:
                    return True
            else:
                if top.left:
                    top.left.val = top.val + top.left.val
                    q.put(top.left)
        
                if top.right:
                    top.right.val = top.val + top.right.val
                    q.put(top.right)
        return False
                
            

# Using Recursion:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0 
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
