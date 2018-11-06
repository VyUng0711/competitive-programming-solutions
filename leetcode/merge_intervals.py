# https://leetcode.com/problems/merge-intervals/description/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e



class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        
        si = sorted(intervals, key= lambda x: (x.start, x.end))
        
        # print([(x.start, x.end) for x in si])
        
        stack = [si[0]]
        for i in range(1, len(si)):
            if si[i].start >= stack[-1].start and si[i].start <= stack[-1].end:
    
                merged = Interval(min(stack[-1].start, si[i].start), max(stack[-1].end, si[i].end))
                stack.pop()
                stack.append(merged)
            else:
                stack.append(si[i])
            # print(stack)
        return stack 


