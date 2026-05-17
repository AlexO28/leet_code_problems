# You are given two integer arrays nums1 and nums2 of length n.
# The XOR sum of the two integer arrays is (nums1[0] XOR nums2[0]) + (nums1[1] XOR nums2[1]) + ... + (nums1[n - 1] XOR nums2[n - 1]) (0-indexed).
# For example, the XOR sum of [1,2,3] and [3,2,1] is equal to (1 XOR 3) + (2 XOR 2) + (3 XOR 1) = 2 + 0 + 2 = 4.
# Rearrange the elements of nums2 such that the resulting XOR sum is minimized.
# Return the XOR sum after the rearrangement.
from math import inf
from typing import List


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        num = 1 << len(nums2)
        f = [inf] * num
        f[0] = 0
        for i in range(1, num):
            k = i.bit_count() - 1
            for j in range(len(nums2)):
                if i >> j & 1:
                    f[i] = min(f[i], f[i ^ (1 << j)] + (nums1[k] ^ nums2[j]))
        return f[-1]
