# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        cur = root
        closest = None
        cur_dist = float('inf')
        while cur:
            if cur.val == target:
                closest = cur.val
                return closest
            elif cur.val < target and cur.right:
                if abs(cur.val - target) < abs(cur.right.val - target):
                    if abs(cur.val - target) < cur_dist:
                        closest = cur.val
                        cur_dist = abs(cur.val - target)
                else:
                    if abs(cur.right.val - target) < cur_dist:
                        closest = cur.right.val
                        cur_dist = abs(cur.right.val - target)
                cur = cur.right
                
            elif cur.val > target and cur.left:
                if abs(cur.val - target) < abs(cur.left.val - target):
                    if abs(cur.val - target) < cur_dist:
                        closest = cur.val
                        cur_dist = abs(cur.val - target)
                else:
                    if abs(cur.left.val - target) < cur_dist:
                        closest = cur.left.val
                        cur_dist = abs(cur.left.val - target)
                cur = cur.left
            else:
                if abs(cur.val - target) < cur_dist:
                    closest = cur.val
                    cur_dist = abs(cur.val - target)
                return closest
        return closest

# Better solution:
class Solution:
    def closestValue(self, root, target):
        cur = root
        closest = cur.val
        while cur:
            if abs(cur.val - target) < abs(closest - target):
                closest = cur.val
            if cur.val == target:
                return cur.val
            elif cur.val < target:
                cur = cur.right
            else:
                cur = cur.left
        return closest
