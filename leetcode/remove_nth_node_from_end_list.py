# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Method 1: Two pass:

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        # print(length)
        
        print('head', head.val)
        cur = dummy
        stop = length - n
        while stop > 0:
            stop -= 1
            cur = cur.next
            print(cur.val)
        cur.next = cur.next.next
        return dummy.next

# Method 2: One pass:

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n + 1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
