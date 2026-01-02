# You are given two groups of points where the first group has size1 points, the second group has size2 points, and size1 >= size2.
# The cost of the connection between any two points are given in an size1 x size2 matrix where cost[i][j] is the cost of connecting point i of the first group and point j of the second group. The groups are connected if each point in both groups is connected to one or more points in the opposite group. In other words, each point in the first group must be connected to at least one point in the second group, and each point in the second group must be connected to at least one point in the first group.
# Return the minimum cost it takes to connect the two groups.
from typing import List


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        f = [[inf] * (1 << len(cost[0])) for _ in range(len(cost) + 1)]
        f[0][0] = 0
        for i in range(1, len(cost) + 1):
            for j in range(1 << len(cost[0])):
                for k in range(len(cost[0])):
                    if (j >> k & 1) == 0:
                        continue
                    c = cost[i - 1][k]
                    x = min(f[i][j ^ (1 << k)], f[i - 1][j], f[i - 1][j ^ (1 << k)]) + c
                    f[i][j] = min(f[i][j], x)
        return f[len(cost)][-1]
