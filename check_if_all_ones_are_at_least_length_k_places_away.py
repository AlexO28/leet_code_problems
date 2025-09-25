# Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return True
        one_pos = None
        for j in range(len(nums)):
            if nums[j] == 1:
                if one_pos is None:
                    one_pos = j
                else:
                    if j - one_pos - 1 < k:
                        return False
                    else:
                        one_pos = j
        return True
