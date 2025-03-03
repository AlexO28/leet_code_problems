# You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:
# Every element less than pivot appears before every element greater than pivot.
# Every element equal to pivot appears in between the elements less than and greater than pivot.
# The relative order of the elements less than pivot and the elements greater than pivot is maintained.
# Return nums after the rearrangement.
from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        if len(nums) == 1:
            return nums
        else:
            nums_before = []
            nums_after = []
            nums_equal = []
            for num in nums:
                if num < pivot:
                    nums_before.append(num)
                elif num == pivot:
                    nums_equal.append(num)
                else:
                    nums_after.append(num)
            nums_before.extend(nums_equal)
            nums_before.extend(nums_after)
            return nums_before
