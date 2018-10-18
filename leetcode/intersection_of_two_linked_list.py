# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Method 1: get the lengths of two linked lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        def get_len(head):
            res = 0
            while head:
                res += 1
                head = head.next
            return res
        
        def traverse(longer, shorter, diff):
            for i in range(diff):
                longer = longer.next
            while longer and shorter:
                if longer.val == shorter.val:
                    return longer
            return None
        
            
        lenA = get_len(headA)
        lenB = get_len(headB)
        diff = abs(lenA - lenB)
        if lenA > lenB:
            return traverse(headA, headB, diff)
        else:
            return traverse(headB, headA, diff)
        
            
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

# Method 2:

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        A_pointer = headA
        B_pointer = headB
        while A_pointer != B_pointer:
            if A_pointer:
                A_pointer = A_pointer.next
            else:
                A_pointer = headB
            if B_pointer:
                B_pointer = B_pointer.next
            else:
                B_pointer = headA
        return A_pointer


