# You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each row of blocks contains one less block than the row beneath it and is centered on top.
# To make the pyramid aesthetically pleasing, there are only specific triangular patterns that are allowed. A triangular pattern consists of a single block stacked on top of two blocks. The patterns are given as a list of three-letter strings allowed, where the first two characters of a pattern represent the left and right bottom blocks respectively, and the third character is the top block.
# For example, "ABC" represents a triangular pattern with a 'C' block stacked on top of an 'A' (left) and 'B' (right) block. Note that this is different from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom.
# You start with a bottom row of blocks bottom, given as a single string, that you must use as the base of the pyramid.
# Given bottom and allowed, return true if you can build the pyramid all the way to the top such that every triangular pattern in the pyramid is in allowed, or false otherwise.
from itertools import product
from functools import cache
from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        self.transition_dict = defaultdict(list)
        for block_left, block_right, block_top in allowed:
            self.transition_dict[block_left, block_right].append(block_top)
        return self.build_pyramid(bottom)

    @cache
    def build_pyramid(self, current_level):
        if len(current_level) == 1:
            return True
        next_level_options = []
        for i in range(len(current_level)-1):
            possible_blocks = self.transition_dict[current_level[i], current_level[i+1]]
            if not possible_blocks:
                return False
            next_level_options.append(possible_blocks)
        return any(self.build_pyramid(''.join(next_level)) for next_level in product(*next_level_options))
