# Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. The objective of the game is to end with the most stones.
# Alice and Bob take turns, with Alice starting first.
# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). Initially, M = 1.
# The game continues until all the stones have been taken.
# Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
from typing import List
from functools import cache
from itertools import accumulate


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        self.total_piles = len(piles)
        self.prefix_sums = list(accumulate(piles, initial = 0))
        return self.search(0, 1)

    @cache
    def search(self, current_index, max_take):
        if 2 * max_take >= self.total_piles - current_index:
            return self.prefix_sums[self.total_piles] - self.prefix_sums[current_index]
        else:
            return max(self.prefix_sums[self.total_piles] - self.prefix_sums[current_index] - self.search(current_index + x, max(max_take, x)) for x in range(1, 2 * max_take + 1))
