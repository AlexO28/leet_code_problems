# Given an integer array nums and an integer k, return the number of good subarrays of nums.
# A good array is an array where the number of different integers in that array is exactly k.
# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.
from collections import Counter
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        arr1 = self.at_most_k_distance(k-1, nums)
        arr2 = self.at_most_k_distance(k, nums)
        return sum(arr1[j]-arr2[j] for j in range(min(len(arr1), len(arr2))))


    def at_most_k_distance(self, k, nums):
        start_positions = [0]*(len(nums))
        count = Counter()
        left = 0
        for j in range(len(nums)):
            count[nums[j]] += 1
            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            start_positions[j] = left
        return start_positions
