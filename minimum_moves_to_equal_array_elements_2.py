# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
# In one move, you can increment or decrement an element of the array by 1.
import numpy as np


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        mode = round(np.median(nums))
        return sum([abs(num-mode) for num in nums])
