# https://leetcode.com/problems/next-greater-element-ii/description/

# O(N^2)
class Solution:
    def nextGreaterElements(self, nums):
        out = []
        for i in range(len(nums)):
            j = i + 1
            count = 0
            found = False
            while count < len(nums):
                if nums[j % len(nums)] > nums[i]:
                    out.append(nums[j % len(nums)])
                    found = True
                    break
                else:
                    j += 1
                    count += 1
            if not found:
                out.append(-1)
        return out
           
# O(N)
class Solution:
    def nextGreaterElements(self, nums):
        result = [-1] * len(nums)
        stack = [i for i in range(len(nums) - 1, - 1, -1)]
        
        for i in range(len(nums) - 1, -1, -1):
            print(stack)
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                result[i] = nums[stack[-1]]
            stack.append(i)
            
        return result 
