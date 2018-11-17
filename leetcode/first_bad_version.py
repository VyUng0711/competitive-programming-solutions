# https://leetcode.com/problems/first-bad-version/description/
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


# Another version:
class Solution:
    def firstBadVersion(self, n):
        low = 1
        high = n
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low
                
        
