# You are given a 0-indexed integer array nums. For each index i (1 <= i <= nums.length - 2) the beauty of nums[i] equals:
# 2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
# 1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
# 0, if none of the previous conditions holds.
# Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.
from math import inf
from typing import List


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        max_val = -1
        prefixes = []
        for num in nums:
            max_val = max(max_val, num)
            prefixes.append(max_val)
        suffixes = []
        min_val = inf
        for num in nums[::-1]:
            min_val = min(min_val, num)
            suffixes.append(min_val)
        suffixes = suffixes[::-1]
        summa = 0
        for i in range(1, len(nums) - 1):
            if prefixes[i - 1] < nums[i] < suffixes[i + 1]:
                summa += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                summa += 1
        return summa
