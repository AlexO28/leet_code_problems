# There exist n rectangles in a 2D plane with edges parallel to the x and y axis. You are given two 2D integer arrays bottomLeft and topRight where bottomLeft[i] = [a_i, b_i] and topRight[i] = [c_i, d_i] represent the bottom-left and top-right coordinates of the ith rectangle, respectively.
# You need to find the maximum area of a square that can fit inside the intersecting region of at least two rectangles. Return 0 if such a square does not exist.
from typing import List


class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        max_area = 0
        for i in range(len(bottomLeft) - 1):
            for j in range(i + 1, len(bottomLeft)):
                if bottomLeft[i][0] > topRight[j][0]:
                    continue
                if bottomLeft[i][1] > topRight[j][1]:
                    continue
                if bottomLeft[j][0] > topRight[i][0]:
                    continue
                if bottomLeft[j][1] > topRight[i][1]:
                    continue
                side_x = min(topRight[i][0], topRight[j][0]) - max(
                    bottomLeft[i][0], bottomLeft[j][0]
                )
                side_y = min(topRight[i][1], topRight[j][1]) - max(
                    bottomLeft[i][1], bottomLeft[j][1]
                )
                cur_area = min(side_x, side_y) ** 2
                max_area = max(max_area, cur_area)
        return max_area
