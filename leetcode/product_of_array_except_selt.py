# https://leetcode.com/problems/product-of-array-except-self/description/
# Not allowed to use DIVISION!
# Method 1: extra space, runtime O(n)
class Solution(object):
    def productExceptSelf(self, nums):
        from_left = [1]
        for i in range(0, len(nums) - 1):
            from_left.append(from_left[-1] * nums[i])
        from_right = [1]

        for j in range(len(nums) - 1, 0, -1):
            from_right.append(from_right[-1] * nums[j])
        from_right = list(reversed(from_right))
        result = []
        for k in range(len(from_left)):
            result.append(from_left[k] * from_right[k])
        # print(from_left)
        # print(from_right)
        return result

            
# Method 2: no extra space, runtime O(n)
class Solution(object):
    def productExceptSelf(self, nums):
        from_left = [1]
        for i in range(0, len(nums) - 1):
            from_left.append(from_left[-1] * nums[i])
        from_right = 1
        for j in range(len(nums) - 2, -1, -1):
            from_right = from_right * nums[j + 1]
            from_left[j] = from_left[j] * from_right
        return from_left
