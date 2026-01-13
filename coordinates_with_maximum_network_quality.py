# You are given an array of network towers towers, where towers[i] = [xi, yi, qi] denotes the ith network tower with location (xi, yi) and quality factor qi. All the coordinates are integral coordinates on the X-Y plane, and the distance between the two coordinates is the Euclidean distance.
# You are also given an integer radius where a tower is reachable if the distance is less than or equal to radius. Outside that distance, the signal becomes garbled, and the tower is not reachable.
# The signal quality of the ith tower at a coordinate (x, y) is calculated with the formula ⌊qi / (1 + d)⌋, where d is the distance between the tower and the coordinate. The network quality at a coordinate is the sum of the signal qualities from all the reachable towers.
# Return the array [cx, cy] representing the integral coordinate (cx, cy) where the network quality is maximum. If there are multiple coordinates with the same network quality, return the lexicographically minimum non-negative coordinate.
# Note:
# A coordinate (x1, y1) is lexicographically smaller than (x2, y2) if either:
# x1 < x2, or
# x1 == x2 and y1 < y2.
# ⌊val⌋ is the greatest integer less than or equal to val (the floor function).
import numpy as np
from typing import List


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        max_quality = -1
        best_x = -1
        best_y = -1
        for x in range(0, 51):
            for y in range(0, 51):
                total_quality = 0
                for tower in towers:
                    d = ((tower[0] - x) ** 2 + (tower[1] - y) ** 2) ** 0.5 
                    if d <= radius:
                        total_quality += np.floor(tower[-1] / (1 + d))
                if total_quality > max_quality:
                    best_x = x
                    best_y = y
                    max_quality = total_quality
        return [best_x, best_y]
