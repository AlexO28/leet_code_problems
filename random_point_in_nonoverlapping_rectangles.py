# You are given an array of non-overlapping axis-aligned rectangles rects where rects[i] = [ai, bi, xi, yi] indicates that (ai, bi) is the bottom-left corner point of the ith rectangle and (xi, yi) is the top-right corner point of the ith rectangle. Design an algorithm to pick a random integer point inside the space covered by one of the given rectangles. A point on the perimeter of a rectangle is included in the space covered by the rectangle.
# Any integer point inside the space covered by one of the given rectangles should be equally likely to be returned.
import random
from bisect import bisect_left

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = []
        area = 0
        for rect in rects:
            area += (rect[2]-rect[0]+1)*(rect[3]-rect[1]+1)
            self.areas.append(area)
        
    def pick(self) -> List[int]:
        ind = random.randint(1, self.areas[-1])
        num = bisect_left(self.areas, ind)
        return [random.randint(self.rects[num][0], self.rects[num][2]),
                random.randint(self.rects[num][1], self.rects[num][3])]
