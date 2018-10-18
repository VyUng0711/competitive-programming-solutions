# https://leetcode.com/problems/linked-list-cycle/description/

# Method 1: Using hash table
class Solution(object):
    def hasCycle(self, head):
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False

# Method 2: Using Floyd cycle detection algorithm
class Solution(object):
    def hasCycle(self, head):
        i = head
        j = head
        while i and j and j.next:
            i = i.next
            j = j.next.next 
            if i == j:
                return True
        return False

