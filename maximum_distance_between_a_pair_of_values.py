# You are given two non-increasing 0-indexed integer arrays nums1​​​​​​ and nums2​​​​​​.
# A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i​​​​.
# Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.
# An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.
from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        j_prev = 0
        max_dist = 0
        for i in range(len(nums1)):
            decrease = False
            for j in range(j_prev, len(nums2)):
                if nums2[j] < nums1[i]:
                    decrease = True
                    break
            if decrease:
                j_prev = max(j - 1, 0)
            else:
                j_prev = j
            max_dist = max(max_dist, j_prev - i)
        return max_dist
