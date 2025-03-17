# You are given an integer array nums consisting of 2 * n integers.
# You need to divide nums into n pairs such that:
# Each element belongs to exactly one pair.
# The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                if freq_dict[num] == 1:
                    freq_dict[num] = 0
                else:
                    freq_dict[num] = 1
            else:
                freq_dict[num] = 1
        for num in freq_dict:
            if freq_dict[num] == 1:
                return False
        return True
