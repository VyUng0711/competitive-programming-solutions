# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, J, S):
        look_up = {x for x in J}
        count = 0
        for stone in S:
            if stone in look_up:
                count += 1
        return count
