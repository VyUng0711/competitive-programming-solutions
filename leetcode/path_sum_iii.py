# https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.count = 0
        cache = {0: 1}
        self.recurse(root, sum, 0, cache)
        return self.count
    
    def recurse(self, root, sum, cur_sum, cache):
        if not root:
            return 0
        cur_sum += root.val
        self.count += cache.get(cur_sum - sum, 0)
        cache[cur_sum] = cache.get(cur_sum, 0) + 1

        self.recurse(root.left, sum, cur_sum, cache)
        self.recurse(root.right, sum, cur_sum, cache)

        cache[cur_sum] -= 1
          


