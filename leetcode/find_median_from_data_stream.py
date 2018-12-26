# https://leetcode.com/problems/find-median-from-data-stream/

import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num):
        heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))
        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        """
        :type num: int
        :rtype: void
        """
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] + (-self.max_heap[0])) / 2
        else:
            return self.min_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


