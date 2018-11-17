# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self, head):
        new_head = None
        while head: 
            cur = head
            head = head.next
            cur.next = new_head
            new_head = cur
        return new_head
    
    def isPalindrome(self, head):
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
            
        pointer = head
        for i in range(length // 2):
            pointer = pointer.next
            
        new_head = self.reverse(pointer)
        print(new_head.val)
        i = new_head
        j = head
        while i and j:
            if i.val != j.val:
                return False
            i = i.next
            j = j.next
        return True
        
        """
        :type head: ListNode
        :rtype: bool
        """

