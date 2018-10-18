# https://leetcode.com/problems/reverse-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Recursive:

class Solution:
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
#Iterative

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev    
