# https://leetcode.com/problems/paint-house/description/

# class Solution(object):
    def minCost(self, costs):
        red = 0
        blue = 0
        green = 0
        for r, b, g in costs:
            red, blue, green = r + min(blue, green), b + min(red, green), g + min(red, blue)
            # cur_red = r + min(blue, green)
            # cur_blue = b + min(red, green)
            # cur_green = g + min(red, blue)
            # red = cur_red
            # blue = cur_blue
            # green = cur_green
            
        return min(red, blue, green)


