# https://leetcode.com/problems/min-cost-climbing-stairs/description/


class Solution(object):
    def minCostClimbingStairs(self, cost):
        dp = [0] * (len(cost))
        if not cost:
            return 0
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost)

        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
            
        # print(dp)
        return min(dp[-1], dp[-2])



class Solution(object):
    def minCostClimbingStairs(self, cost):
        dp = [0] * (len(cost) + 1)
        if not cost:
            return 0
        if len(cost) == 1:
            return cost[0]
        
        
        pre_one = cost[1]
        pre_two = cost[0]
        min_cost = 0
        for i in range(2, len(cost)):
            min_cost = cost[i] + min(pre_one, pre_two)
            pre_two = pre_one
            pre_one = min_cost
        return min(pre_one, pre_two)


