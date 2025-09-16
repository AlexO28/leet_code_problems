# You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.
# Choose at most k different engineers out of the n engineers to form a team with the maximum performance.
# The performance of a team is the sum of its engineers' speeds multiplied by the minimum efficiency among its engineers.
# Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.
from typing import List
import heapq


class Solution:
    def maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        engineers = sorted(zip(speed, efficiency), key=lambda x: -x[1])
        max_performance = 0
        total_speed = 0
        speed_heap = []
        for current_speed, current_efficiency in engineers:
            total_speed += current_speed
            max_performance = max(max_performance, total_speed * current_efficiency)
            heapq.heappush(speed_heap, current_speed)
            if len(speed_heap) == k:
                total_speed -= heapq.heappop(speed_heap)
        return max_performance % (10**9 + 7)
