# You want to build n new buildings in a city. The new buildings will be built in a line and are labeled from 1 to n.
# However, there are city restrictions on the heights of the new buildings:
# The height of each building must be a non-negative integer.
# The height of the first building must be 0.
# The height difference between any two adjacent buildings cannot exceed 1.
# Additionally, there are city restrictions on the maximum height of specific buildings. These restrictions are given as a 2D integer array restrictions where restrictions[i] = [idi, maxHeighti] indicates that building idi must have a height less than or equal to maxHeighti.
# It is guaranteed that each building will appear at most once in restrictions, and building 1 will not be in restrictions.
# Return the maximum possible height of the tallest building.
from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])
        for i in range(1, len(restrictions)):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + restrictions[i][0] - restrictions[i - 1][0],
            )
        for i in range(len(restrictions) - 2, 0, -1):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + restrictions[i + 1][0] - restrictions[i][0],
            )
        ans = 0
        for i in range(len(restrictions) - 1):
            ans = max(
                ans,
                (
                    restrictions[i][1]
                    + restrictions[i + 1][1]
                    + restrictions[i + 1][0]
                    - restrictions[i][0]
                )
                // 2,
            )
        return ans
