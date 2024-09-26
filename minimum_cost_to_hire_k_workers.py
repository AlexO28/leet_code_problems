# There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.
# We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:
# Every worker in the paid group must be paid at least their minimum wage expectation.
# In the group, each worker's pay must be directly proportional to their quality. This means if a worker’s quality is double that of another worker in the group, then they must be paid twice as much as the other worker.
# Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within 10-5 of the actual answer will be accepted.
import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        min_cost = None
        total_quality = 0
        max_heap = []
        for cur_quality, cur_wage, cur_efficiency in sorted(zip(quality, wage, [wage[j]/quality[j] for j in range(len(quality))]), key=lambda x: x[2]):
            total_quality += cur_quality
            heapq.heappush(max_heap, -cur_quality)
            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)
            if len(max_heap) == k:
                if min_cost is None:
                    min_cost = total_quality * cur_efficiency
                else:
                    min_cost = min(min_cost, total_quality * cur_efficiency)
        return min_cost
