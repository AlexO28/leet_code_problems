# You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.
# Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.
# Answers within 10-5 of the actual answer will be accepted.
# Note: Squares may overlap. Overlapping areas should be counted multiple times.
from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        self.squares = squares
        self.s = sum(a[2] * a[2] for a in self.squares)
        l = 0
        r = max(a[1] + a[2] for a in self.squares)
        eps = 0.00001
        while r - l > eps:
            mid = (l + r) / 2
            if self.check(mid):
                r = mid
            else:
                l = mid
        return r

    def check(self, y1):
        t = 0
        for x, y, l in self.squares:
            if y < y1:
                t += l * min(y1 - y, l)
        return t >= self.s / 2
