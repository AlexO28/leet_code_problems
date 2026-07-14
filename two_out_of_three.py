# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.
from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        for num in nums1:
            if (num in nums2) or (num in nums3):
                res.append(num)
        for num in nums2:
            if (num in nums1) or (num in nums3):
                res.append(num)
        for num in nums3:
            if (num in nums1) or (num in nums2):
                res.append(num)
        return list(set(res))
