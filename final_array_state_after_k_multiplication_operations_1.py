# You are given an integer array nums, an integer k, and an integer multiplier.
# You need to perform k operations on nums. In each operation:
# Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
# Replace the selected minimum value x with x * multiplier.
# Return an integer array denoting the final state of nums after performing all k operations.
import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums
        res = [0] * len(nums)
        minHeap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(minHeap)
        for i in range(k):
            num, i = heapq.heappop(minHeap)
            heapq.heappush(minHeap, (num * multiplier, i))
        for num, i in minHeap:
            res[i] = num
        return res
