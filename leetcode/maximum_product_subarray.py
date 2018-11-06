# https://leetcode.com/problems/maximum-product-subarray/description/

class Solution(object):
    def maxProduct(self, nums):
        
        pos = [1] * len(nums)
        neg = [1] * len(nums)
        
        max_pos = nums[0]
        for i in range(len(nums)):
            if nums[i] > 0:
                neg[i] = neg[i - 1] * nums[i]
                pos[i] = max(pos[i - 1] * nums[i], nums[i])
            else:
                pos[i] = neg[i - 1] * nums[i]
                neg[i] = min(pos[i - 1] * nums[i], nums[i])
                
            max_pos = max(max_pos, pos[i])
        
        return max_pos

class Solution(object):
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        print(A)
        print(B)
        return max(A + B)


