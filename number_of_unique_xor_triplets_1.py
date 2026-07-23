# You are given an integer array nums of length n, where nums is a permutation of the numbers in the range [1, n].
# A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.
# Return the number of unique XOR triplet values from all possible triplets (i, j, k).
from typing import List
from math import log


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        elif len(nums) == 2:
            return len(
                set(
                    {
                        nums[0],
                        nums[1],
                        nums[0] ^ nums[0] ^ nums[1],
                        nums[0] ^ nums[1] ^ nums[1],
                    }
                )
            )
        else:
            return 2 * 2 ** int(log(len(nums)) / log(2))
