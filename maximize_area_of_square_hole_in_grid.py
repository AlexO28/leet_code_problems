# You are given the two integers, n and m and two integer arrays, hBars and vBars. The grid has n + 2 horizontal and m + 2 vertical bars, creating 1 x 1 unit cells. The bars are indexed starting from 1.
# You can remove some of the bars in hBars from horizontal bars and some of the bars in vBars from vertical bars. Note that other bars are fixed and cannot be removed.
# Return an integer denoting the maximum area of a square-shaped hole in the grid, after removing some bars (possibly none).
from typing import List


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        range_horizontal = self.find_range(hBars)
        range_vertical = self.find_range(vBars)
        return min(range_horizontal + 1, range_vertical + 1) ** 2

    def find_range(self, arr):
        arr.sort()
        max_len = 0
        cur_elem = -1
        cur_len = 0
        for elem in arr:
            cur_elem += 1
            if elem == cur_elem:
                cur_len += 1
            else:
                max_len = max(max_len, cur_len)
                cur_elem = elem
                cur_len = 1
        return max(max_len, cur_len)
