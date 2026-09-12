# You are given an array of non-negative integers nums and an integer k. In one operation, you may choose any element from nums and increment it by 1.
# Return the maximum product of nums after at most k operations. Since the answer may be very large, return it modulo 109 + 7. Note that you should maximize the product before taking the modulo. 
import heapq
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for j in range(k):
            elem = heapq.heappop(nums)
            heapq.heappush(nums, elem + 1)
        prod = 1
        MOD = 1000000007
        while nums:
            prod = prod * heapq.heappop(nums) % MOD
        return prod
