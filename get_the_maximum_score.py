# You are given two sorted arrays of distinct integers nums1 and nums2.
# A valid path is defined as follows:
# Choose array nums1 or nums2 to traverse (from index-0).
# Traverse the current array from left to right.
# If you are reading any value that is present in nums1 and nums2 you are allowed to change your path to the other array. (Only one repeated value is considered in the valid path).
# The score is defined as the sum of unique values in a valid path.
# Return the maximum score you can obtain of all possible valid paths. Since the answer may be too large, return it modulo 109 + 7.
from typing import List


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        pointer1 = 0
        pointer2 = 0
        sum_path1 = 0
        sum_path2 = 0
        while pointer1 < len(nums1) or pointer2 < len(nums2):
            if pointer1 == len(nums1):
                sum_path2 += nums2[pointer2]
                pointer2 += 1
            elif pointer2 == len(nums2):
                sum_path1 += nums1[pointer1]
                pointer1 += 1
            elif nums1[pointer1] < nums2[pointer2]:
                sum_path1 += nums1[pointer1]
                pointer1 += 1
            elif nums1[pointer1] > nums2[pointer2]:
                sum_path2 += nums2[pointer2]
                pointer2 += 1
            else:
                sum_path1 = max(sum_path1, sum_path2) + nums1[pointer1]
                sum_path2 = sum_path1
                pointer1 += 1
                pointer2 += 1
        return max(sum_path1, sum_path2) % MOD
