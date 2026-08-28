# You are given a 0-indexed integer array nums. You are allowed to permute nums into a new array perm of your choosing.
# We define the greatness of nums be the number of indices 0 <= i < nums.length for which perm[i] > nums[i].
# Return the maximum possible greatness you can achieve after permuting nums.
from typing import List
from collections import Counter


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        freq_dict = Counter(nums)
        keys = list(freq_dict.keys())
        keys.sort()
        greatness = 0
        ind = 0
        for num in nums:
            if keys[ind] == num:
                ind += 1
                if ind == len(keys):
                    break
            freq_dict[keys[ind]] -= 1
            greatness += 1
            if freq_dict[keys[ind]] == 0:
                ind += 1
                if ind == len(keys):
                    break
        return greatness
