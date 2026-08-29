# You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
# The length of the subarray is k, and
# All the elements of the subarray are distinct.
# Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.
# A subarray is a contiguous non-empty sequence of elements within an array.
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        counts = {}
        cur_sum = 0
        for j in range(len(nums)):
            if nums[j] in counts:
                counts[nums[j]] += 1
            else:
                counts[nums[j]] = 1
            cur_sum += nums[j]
            if j >= k:
                cur_sum -= nums[j - k]
                if counts[nums[j - k]] == 1:
                    del counts[nums[j - k]]
                else:
                    counts[nums[j - k]] -= 1
            if len(counts) == k:
                max_sum = max(max_sum, cur_sum)
        return max_sum
