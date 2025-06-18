# You are given an integer array nums of size n where n is a multiple of 3 and a positive integer k.
# Divide the array nums into n / 3 arrays of size 3 satisfying the following condition:
# The difference between any two elements in one array is less than or equal to k.
# Return a 2D array containing the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.
from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        groups = []
        start = 0
        delta = len(nums) // 3
        end = 3
        for j in range(delta):
            group = []
            prev_num = nums[start]
            for i in range(start, end):
                group.append(nums[i])
                if nums[i] - prev_num > k:
                    return []
            groups.append(group)
            start = end
            end += 3
        return groups
