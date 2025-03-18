# A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
# Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
from typing import List
import numpy as np


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = np.array([cost[1]-cost[0] for cost in costs])
        costs = np.array(costs)
        costs = costs[np.argsort(diffs)]
        res = 0
        half = len(costs) // 2
        for i in range(half):
            res += costs[i][1]
        for i in range(half, len(costs)):
            res += costs[i][0]
        return int(res)
