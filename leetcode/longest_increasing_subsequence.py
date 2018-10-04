# https://leetcode.com/problems/longest-increasing-subsequence/submissions/1

# O(n^2)
class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        storage = [0] * len(nums)
        storage[0] = 1

        for i in range(1, len(nums)):
            storage[i] = 1
            for j in range(0, i):
                if nums[j] < nums[i]: 
                    storage[i] = max(storage[j] + 1, storage[i])
        max_len = max(storage)   
        return max_len

# O(n logn)
class Solution:
    def lengthOfLIS(self, nums):
        lis = []
        for a in nums:
            replace_point = bisect.bisect_left(lis, a, 0, len(lis))
            if replace_point == len(lis):
                lis.append(a)
            else:
                lis[replace_point] = a
        return len(lis)
