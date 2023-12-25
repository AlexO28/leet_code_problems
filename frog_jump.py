# A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.
# Given a list of stones positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.
# If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.
from functools import lru_cache

class Solution:
    def canCross(self, stones: List[int]) -> bool:

        @lru_cache(maxsize=None)
        def dfs(index, jump_size):
            if index == len(stones) - 1:
                return True
            for next_jump in range(jump_size - 1, jump_size + 2):
                if next_jump > 0 and stones[index] + next_jump in stone_positions:
                    if dfs(stone_positions[stones[index] + next_jump], next_jump):
                        return True
            return False
