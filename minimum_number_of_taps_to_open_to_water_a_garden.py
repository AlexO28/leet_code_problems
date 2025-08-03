# There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e., the length of the garden is n).
# There are n + 1 taps located at points [0, 1, ..., n] in the garden.
# Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.
# Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.
from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_right_from_left = [0] * (n + 1)
        for tap_index, tap_range in enumerate(ranges):
            left_bound = max(0, tap_index - tap_range)
            right_bound = tap_index + tap_range
            max_right_from_left[left_bound] = max(
                max_right_from_left[left_bound], right_bound
            )
        taps_required = 0
        max_covered_so_far = 0
        previous_max = 0
        for pos in range(n):
            max_covered_so_far = max(max_covered_so_far, max_right_from_left[pos])
            if max_covered_so_far <= pos:
                return -1
            if previous_max == pos:
                taps_required += 1
                previous_max = max_covered_so_far
        return taps_required
