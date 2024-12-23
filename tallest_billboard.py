# You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. Each steel support must be an equal height.
# You are given a collection of rods that can be welded together. For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.
# Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.
from typing import List
from math import inf


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        total_length = sum(rods)
        dp_table = [[-inf] * (total_length + 1) for i in range(len(rods) + 1)]
        dp_table[0][0] = 0
        current_sum = 0
        for i in range(1, len(rods) + 1):
            current_sum += rods[i-1]
            for j in range(current_sum + 1):
                dp_table[i][j] = dp_table[i-1][j]
                if j >= rods[i-1]:
                    dp_table[i][j] = max(dp_table[i][j], dp_table[i - 1][j - rods[i-1]])
                else:
                    delta = rods[i-1] - j
                    dp_table[i][j] = max(dp_table[i][j], dp_table[i - 1][delta] + delta)
                if j + rods[i-1] <= current_sum:
                    dp_table[i][j] = max(dp_table[i][j], dp_table[i - 1][j + rods[i-1]] + rods[i-1])
        return dp_table[len(rods)][0]
