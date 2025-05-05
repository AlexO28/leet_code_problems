# Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.
# An array A is a zigzag array if either:
# Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
# OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
# Return the minimum number of moves to transform the given array nums into a zigzag array.
from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        min_moves_1 = 0
        for j in range(1, len(nums), 2):
            if j < len(nums) - 1:
                min_val = min(nums[j-1], nums[j+1])
            else:
                min_val = nums[j-1]
            if nums[j] >= min_val:
                min_moves_1 += nums[j] - min_val + 1
        min_moves_2 = 0
        for j in range(0, len(nums), 2):
            if j == 0:
                min_val = nums[1]
            elif j == len(nums) - 1:
                min_val = nums[j - 1]
            else:
                min_val = min(nums[j-1], nums[j+1])
            if nums[j] >= min_val:
                min_moves_2 += nums[j] - min_val + 1
        return min(min_moves_1, min_moves_2)
