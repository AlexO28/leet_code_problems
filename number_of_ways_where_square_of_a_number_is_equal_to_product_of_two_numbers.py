# Given two arrays of integers nums1 and nums2, return the number of triplets formed (type 1 and type 2) under the following rules:
# Type 1: Triplet (i, j, k) if nums1[i]2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k < nums2.length.
# Type 2: Triplet (i, j, k) if nums2[i]2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k < nums1.length.
from typing import List


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        if len(nums2) > 1:
            freq_dict = {}
            for num in nums1:
                square = num**2
                if square in freq_dict:
                    freq_dict[square] += 1
                else:
                    freq_dict[square] = 1
            for i in range(len(nums2)-1):
                for j in range(i+1, len(nums2)):
                    prod = nums2[i] * nums2[j]
                    if prod in freq_dict:
                        res += freq_dict[prod]
        if len(nums1) > 1:
            freq_dict = {}
            for num in nums2:
                square = num**2
                if square in freq_dict:
                    freq_dict[square] += 1
                else:
                    freq_dict[square] = 1
            for i in range(len(nums1)-1):
                for j in range(i+1, len(nums1)):
                    prod = nums1[i] * nums1[j]
                    if prod in freq_dict:
                        res += freq_dict[prod]
        return res
