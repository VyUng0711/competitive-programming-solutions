# https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(-1)
        cur = dummy_head
        carry = 0
        while l1 or l2:
            if l1:
                a = l1.val
            else:
                a = 0
            if l2:
                b = l2.val
            else:
                b = 0
                
            result = a + b + carry
            cur.next = ListNode(result % 10) 
            cur = cur.next
            carry = result // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            cur.next = ListNode(carry)
        return dummy_head.next 
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
