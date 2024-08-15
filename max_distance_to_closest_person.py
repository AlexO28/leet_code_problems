# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).
# There is at least one empty seat, and at least one person sitting.
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
# Return that maximum distance to the closest person.
import numpy as np


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist = 0
        prev_index = None
        for j in range(len(seats)):
            if seats[j] == 1:
                if prev_index is None:
                    max_dist = j
                    prev_index = j
                else:
                    max_dist = max(np.floor((j - prev_index)/2), max_dist)
                    prev_index = j
        if prev_index < len(seats)-1:
            max_dist = max(max_dist, len(seats)-1-prev_index)
        return int(max_dist)
