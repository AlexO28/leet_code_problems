# There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that have been painted last summer should not be painted again.
# A neighborhood is a maximal group of continuous houses that are painted with the same color.
# For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].
# Given an array houses, an m x n matrix cost and an integer target where:
# houses[i]: is the color of the house i, and 0 if the house is not painted yet.
# cost[i][j]: is the cost of paint the house i with the color j + 1.
# Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods. If it is not possible, return -1.
from typing import List


class Solution:
    def minCost(
        self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int
    ) -> int:
        dp = [[[float("inf")] * (target + 1) for _ in range(n + 1)] for _ in range(m)]
        if houses[0] == 0:
            for color_idx, paint_cost in enumerate(cost[0], 1):
                dp[0][color_idx][1] = paint_cost
        else:
            dp[0][houses[0]][1] = 0
        for house_idx in range(1, m):
            if houses[house_idx] == 0:
                for current_color in range(1, n + 1):
                    for num_neighborhoods in range(1, min(target + 1, house_idx + 2)):
                        for prev_color in range(1, n + 1):
                            if current_color == prev_color:
                                dp[house_idx][current_color][num_neighborhoods] = min(
                                    dp[house_idx][current_color][num_neighborhoods],
                                    dp[house_idx - 1][prev_color][num_neighborhoods]
                                    + cost[house_idx][current_color - 1],
                                )
                            else:
                                dp[house_idx][current_color][num_neighborhoods] = min(
                                    dp[house_idx][current_color][num_neighborhoods],
                                    dp[house_idx - 1][prev_color][num_neighborhoods - 1]
                                    + cost[house_idx][current_color - 1],
                                )
            else:
                current_color = houses[house_idx]
                for num_neighborhoods in range(1, min(target + 1, house_idx + 2)):
                    for prev_color in range(1, n + 1):
                        if current_color == prev_color:
                            dp[house_idx][current_color][num_neighborhoods] = min(
                                dp[house_idx][current_color][num_neighborhoods],
                                dp[house_idx - 1][prev_color][num_neighborhoods],
                            )
                        else:
                            dp[house_idx][current_color][num_neighborhoods] = min(
                                dp[house_idx][current_color][num_neighborhoods],
                                dp[house_idx - 1][prev_color][num_neighborhoods - 1],
                            )
        min_cost = min(dp[-1][color][target] for color in range(1, n + 1))
        if min_cost >= float("inf"):
            return -1
        else:
            return min_cost
        
