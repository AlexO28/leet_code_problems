# You have a 1-indexed binary string of length n where all the bits are 0 initially. We will flip all the bits of this binary string (i.e., change them from 0 to 1) one by one. You are given a 1-indexed integer array flips where flips[i] indicates that the bit at index flips[i] will be flipped in the ith step.
# A binary string is prefix-aligned if, after the ith step, all the bits in the inclusive range [1, i] are ones and all the other bits are zeros.
# Return the number of times the binary string is prefix-aligned during the flipping process.
from typing import List


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count_all_blue_moments = 0
        max_bulb_position = 0
        for step_number, bulb_position in enumerate(flips, 1):
            max_bulb_position = max(max_bulb_position, bulb_position)
            if max_bulb_position == step_number:
                count_all_blue_moments += 1
        return count_all_blue_moments
