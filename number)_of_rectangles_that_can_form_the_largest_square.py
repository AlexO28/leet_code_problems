# You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.
# You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.
# Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.
# Return the number of rectangles that can make a square with a side length of maxLen.
from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        rect_dict = {}
        for rectangle in rectangles:
            min_val = min(rectangle[0], rectangle[1])
            if min_val in rect_dict:
                rect_dict[min_val] += 1
            else:
                rect_dict[min_val] = 1
        max_val = max(list(rect_dict.keys()))
        return rect_dict[max_val]
