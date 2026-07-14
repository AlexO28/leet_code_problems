# You are given n rectangles represented by a 0-indexed 2D integer array rectangles, where rectangles[i] = [widthi, heighti] denotes the width and height of the ith rectangle.
# Two rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio. More formally, two rectangles are interchangeable if widthi/heighti == widthj/heightj (using decimal division, not integer division).
# Return the number of pairs of interchangeable rectangles in rectangles.
from typing import List
from math import gcd


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        freq_dict = {}
        for width, height in rectangles:
            div = gcd(width, height)
            width = width/div
            height = height/div
            code = str(width) + "/" + str(height)
            if code in freq_dict:
                freq_dict[code] += 1
            else:
                freq_dict[code] = 1
        summa = 0
        for val in freq_dict.values():
            if val > 1:
                summa += val * (val - 1) // 2
        return summa
