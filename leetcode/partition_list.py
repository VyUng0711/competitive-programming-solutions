# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        small_head = ListNode(0)
        small_head.next = head
        smaller = small_head
        
        large_head = ListNode(0)
        larger = large_head
        
        while smaller.next:
            if smaller.next.val >= x:
                larger.next = smaller.next
                smaller.next = smaller.next.next
                larger.next.next = None  #IMPORTANT
                larger = larger.next
                 
            else:
                smaller = smaller.next
                
        smaller.next = large_head.next
        return small_head.next
        
        

