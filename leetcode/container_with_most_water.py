https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            h = min(height[i], height[j])
            w = j - i
            area = h * w
            max_area = max(max_area, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

