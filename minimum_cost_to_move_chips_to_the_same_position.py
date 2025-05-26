# We have n chips, where the position of the ith chip is position[i].
# We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:
# position[i] + 2 or position[i] - 2 with cost = 0.
# position[i] + 1 or position[i] - 1 with cost = 1.
# Return the minimum cost needed to move all the chips to the same position.
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        freq_dict = {0: 0, 1: 0}
        for elem in position:
            if elem % 2 == 0:
                freq_dict[0] += 1
            else:
                freq_dict[1] += 1
        return min(freq_dict[0], freq_dict[1])
