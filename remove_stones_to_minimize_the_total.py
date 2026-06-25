# You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k. You should apply the following operation exactly k times:
# Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
# Notice that you can apply the operation on the same pile more than once.
# Return the minimum possible total number of stones remaining after applying the k operations.
import heapq
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = []
        for pile in piles:
            heapq.heappush(max_heap, -pile)
        for _ in range(k):
            value = -heapq.heappop(max_heap)
            value -= (value // 2)
            heapq.heappush(max_heap, -value)
        summa = 0
        while max_heap:
            summa -= heapq.heappop(max_heap)
        return summa
