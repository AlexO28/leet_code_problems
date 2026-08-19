# You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.
# The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.
# You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.
# Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.
from typing import List
from collections import deque


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        max_number_of_bombs = 1
        for j in range(len(bombs)):
            cur_visit = deque()
            cur_visit.append(j)
            cur_set = set()
            while cur_visit:
                candidate = cur_visit.pop()
                if candidate not in cur_set:
                    cur_set.add(candidate)
                    for i in range(len(bombs)):
                        if i not in cur_set:
                            if (bombs[i][0] - bombs[candidate][0]) ** 2 + (
                                bombs[i][1] - bombs[candidate][1]
                            ) ** 2 <= bombs[candidate][2] ** 2:
                                cur_visit.append(i)
            max_number_of_bombs = max(max_number_of_bombs, len(cur_set))
        return max_number_of_bombs
