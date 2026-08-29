# You are given a 0-indexed integer array nums having length n, an integer indexDifference, and an integer valueDifference.
# Your task is to find two indices i and j, both in the range [0, n - 1], that satisfy the following conditions:
# abs(i - j) >= indexDifference, and
# abs(nums[i] - nums[j]) >= valueDifference
# Return an integer array answer, where answer = [i, j] if there are two such indices, and answer = [-1, -1] otherwise. If there are multiple choices for the two indices, return any of them.
# Note: i and j may be equal.
from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        prefix_mins = []
        prefix_maxs = []
        min_val = nums[0]
        max_val = nums[0]
        min_ind = 0
        max_ind = 0
        for j in range(len(nums)):
            if nums[j] < min_val:
                min_val = nums[j]
                min_ind = j
            prefix_mins.append(min_ind)
            if nums[j] > max_val:
                max_val = nums[j]
                max_ind = j
            prefix_maxs.append(max_ind)
        for j in range(len(nums)):
            jprev = j - indexDifference
            if jprev >= 0:
                if nums[j] - nums[prefix_mins[jprev]] >= valueDifference:
                    return [j, prefix_mins[jprev]]
                if nums[prefix_maxs[jprev]] - nums[j] >= valueDifference:
                    return [j, prefix_maxs[jprev]]
        return [-1, -1]
