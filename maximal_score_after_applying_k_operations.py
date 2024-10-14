# You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.
# In one operation:
# choose an index i such that 0 <= i < nums.length,
# increase your score by nums[i], and
# replace nums[i] with ceil(nums[i] / 3).
# Return the maximum possible score you can attain after applying exactly k operations.
# The ceiling function ceil(val) is the least integer greater than or equal to val.
import numpy as np
import heapq


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        score = 0
        for j in range(k):
            max_val = heapq.heappop(heap)
            score -= max_val
            heapq.heappush(heap, -np.ceil(-max_val/3))
        return int(score)
