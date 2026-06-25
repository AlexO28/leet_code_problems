# You are given an integer array nums and an integer target.
# Return the number of subarrays of nums in which target is the majority element.
# The majority element of a subarray is the element that appears strictly more than half of the times in that subarray.
from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        count_info = [0]
        counter = 0
        for num in nums:
            if num == target:
                counter += 1
            count_info.append(counter)
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if 2 * (count_info[j + 1] - count_info[i]) > (j - i + 1):
                    res += 1
        return res
