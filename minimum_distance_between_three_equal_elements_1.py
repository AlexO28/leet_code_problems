# You are given an integer array nums.
# A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].
# The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.
# Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.
from typing import List
from math import inf


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        min_dist = inf
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if (nums[i] == nums[j]) and (nums[j] == nums[k]):
                        min_dist = min(min_dist, abs(i - j) + abs(j - k) + abs(k - i))
        if min_dist < inf:
            return min_dist
        else:
            return -1
