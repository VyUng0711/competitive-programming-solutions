# https://leetcode.com/problems/linked-list-cycle-ii/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        i = head
        j = head
        p = None
        while i and j and j.next:
            i = i.next
            j = j.next.next
            if i == j:
                p = i
                break
                
        if p == None:
            return None
        q = head
        while p != q:
            p = p.next
            q = q.next
        return p
