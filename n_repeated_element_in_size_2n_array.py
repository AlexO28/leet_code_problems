# You are given an integer array nums with the following properties:
# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        n = len(nums) // 2
        return [val for val in freq_dict if freq_dict[val] == n][0]
