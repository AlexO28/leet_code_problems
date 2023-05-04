# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.


import numpy as np


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start_pos = 0
        end_pos = len(nums)-1
        if target <= nums[0]:
            return 0
        if target == nums[len(nums)-1]:
            return len(nums)-1
        if target > nums[len(nums)-1]:
            return len(nums)
        while True:
            if end_pos - start_pos == 1:
                return end_pos
            half_pos = (end_pos + start_pos)/2
            middle_pos_1 = int(np.floor(half_pos))
            middle_pos_2 = int(np.ceil(half_pos))
            if target == nums[middle_pos_1]:
                return middle_pos_1
            if target == nums[middle_pos_2]:
                return middle_pos_2
            if target < nums[middle_pos_2]:
                end_pos = middle_pos_2
            elif target > nums[middle_pos_1]:
                start_pos = middle_pos_1
  
