# There is a pizza with 3n slices of varying size, you and your friends will take slices of pizza as follows:
# You will pick any pizza slice.
# Your friend Alice will pick the next slice in the anti-clockwise direction of your pick.
# Your friend Bob will pick the next slice in the clockwise direction of your pick.
# Repeat until there are no more slices of pizzas.
# Given an integer array slices that represent the sizes of the pizza slices in a clockwise direction, return the maximum possible sum of slice sizes that you can pick.
from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        self.slices_to_pick = len(slices) // 3
        return max(
            self.max_sum_non_adjacent(slices[1:]),
            self.max_sum_non_adjacent(slices[:(-1)]),
        )

    def max_sum_non_adjacent(self, nums):
        dp = [[0] * (self.slices_to_pick + 1) for i in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            for j in range(1, self.slices_to_pick + 1):
                if i >= 2:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + nums[i - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], nums[i - 1])
        return dp[-1][self.slices_to_pick]
