# You are given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.
# Return the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length.
# It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.
from typing import List
import heapq
from math import inf


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_value = -inf
        min_heap = []
        for current_x, current_y in points:
            while min_heap and current_x - min_heap[0][1] > k:
                heapq.heappop(min_heap)
            if min_heap:
                max_value = max(max_value, current_x + current_y - min_heap[0][0])
            heapq.heappush(min_heap, (current_x - current_y, current_x))
        return max_value
