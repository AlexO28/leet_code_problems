# You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:
# horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
# verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
# Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.
from typing import List


class Solution:
    def maxArea(
        self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]
    ) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        max_diff_horizontal = max(horizontalCuts[0], h - horizontalCuts[-1])
        if len(horizontalCuts) > 1:
            for j in range(1, len(horizontalCuts)):
                max_diff_horizontal = max(
                    max_diff_horizontal, horizontalCuts[j] - horizontalCuts[j - 1]
                )
        max_diff_vertical = max(verticalCuts[0], w - verticalCuts[-1])
        if len(verticalCuts) > 1:
            for j in range(1, len(verticalCuts)):
                max_diff_vertical = max(
                    max_diff_vertical, verticalCuts[j] - verticalCuts[j - 1]
                )
        return max_diff_horizontal * max_diff_vertical % (10 ** 9 + 7)
