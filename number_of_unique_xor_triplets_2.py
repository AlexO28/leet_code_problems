# You are given an integer array nums.
# A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.
# Return the number of unique XOR triplet values from all possible triplets (i, j, k).
from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        max_val = max(nums) << 1
        data = [False] * max_val
        for a in nums:
            for b in nums:
                data[a ^ b] = True
        res = [0] * max_val
        for ab in range(max_val):
            if data[ab]:
                for c in nums:
                    res[ab ^ c] = 1
        return sum(res)
