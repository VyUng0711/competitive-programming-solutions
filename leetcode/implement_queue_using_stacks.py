# https://leetcode.com/problems/implement-queue-using-stacks/
# Push O(1). Pop O(n), amortized O(1)
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.temp = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.temp:
            while self.queue:
                self.temp.append(self.queue.pop())
        return self.temp.pop()
    
#         if len(self.temp) > 0:
#             return self.temp.pop()
#         else:
#             while len(self.queue) > 0:
#                 self.temp.append(self.queue.pop())
#             return self.temp.pop()
        
            
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.temp:
            while self.queue:
                self.temp.append(self.queue.pop())
        return self.temp[-1]
    
    
        # if len(self.temp) > 0:
        #     return self.temp[-1]
        # else:
        #     while len(self.queue) > 0:
        #         self.temp.append(self.queue.pop())
        #     return self.temp[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.queue) + len(self.temp) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# 

# Push O(1) Pop O(n)
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.temp = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while len(self.queue) > 1:
            self.temp.append(self.queue.pop())
        res = self.queue.pop()
        while len(self.temp) > 0:
            self.queue.append(self.temp.pop())
        return res 

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while len(self.queue) > 0:
            self.temp.append(self.queue.pop())
        res = self.temp[-1]
        while len(self.temp) > 0:
            self.queue.append(self.temp.pop()) 
        return res

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.queue) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
