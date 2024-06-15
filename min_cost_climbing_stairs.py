# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
from functools import cache


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        return min(self.calculateOptimalPrice(0), self.calculateOptimalPrice(1))

    @cache
    def calculateOptimalPrice(self, ind):
        if len(self.cost) - ind <= 2:
            return self.cost[ind]
        else:
            return self.cost[ind] + min(self.calculateOptimalPrice(ind+1), self.calculateOptimalPrice(ind+2))
