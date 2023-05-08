# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.

import numpy as np


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        start_pos = 0
        end_pos = len(nums) - 1
        begin_pos = -1
        while True:
            if nums[start_pos] == target:
                begin_pos = start_pos
                break
            if end_pos == start_pos:
                if nums[start_pos] == target:
                    begin_pos = start_pos
                    break
                else:
                    return [-1, -1]
            elif end_pos - start_pos == 1:
                if nums[start_pos] == target:
                    begin_pos = start_pos
                    break
                elif nums[end_pos] == target:
                    begin_pos = end_pos
                    break
                else:
                    return [-1, -1]
            elif end_pos - start_pos == 2:
                if nums[start_pos] == target:
                    begin_pos = start_pos
                    break
                elif nums[start_pos + 1] == target:
                    begin_pos = start_pos + 1
                    break
                elif nums[end_pos] == target:
                    begin_pos = end_pos
                    break
                else:
                    return [-1, -1]
            middle_pos = int(np.ceil((start_pos + end_pos)/2))
            if nums[middle_pos] >= target:
                end_pos = middle_pos
            else:
                start_pos = middle_pos
    
        fin_pos = -1
        start_pos = begin_pos
        end_pos = len(nums) - 1

        while True:
            if nums[end_pos] == target:
                fin_pos = end_pos
                break
            if end_pos == start_pos:
                if nums[end_pos] == target:
                    fin_pos = end_pos
                    break
                else:
                    return [begin_pos, begin_pos]
            elif end_pos - start_pos == 1:
                if nums[end_pos] == target:
                    fin_pos = end_pos
                    break
                elif nums[start_pos] == target:
                    fin_pos = start_pos
                    break
                else:
                    return [begin_pos, begin_pos]
            elif end_pos - start_pos == 2:
                if nums[end_pos] == target:
                    fin_pos = end_pos
                    break
                elif nums[start_pos + 1] == target:
                    fin_pos = start_pos + 1
                    break
                elif nums[start_pos] == target:
                    fin_pos = start_pos
                    break
                else:
                    return [begin_pos, begin_pos]
            middle_pos = int(np.floor((start_pos + end_pos)/2))
            if nums[middle_pos] <= target:
                start_pos = middle_pos
            else:
                end_pos = middle_pos

        return [begin_pos, fin_pos]
