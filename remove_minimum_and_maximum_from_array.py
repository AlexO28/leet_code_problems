# You are given a 0-indexed array of distinct integers nums.
# There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.
# A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.
# Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.
from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        min_val = nums[0]
        max_val = nums[0]
        min_ind = 0
        max_ind = 0
        for i in range(1, len(nums)):
            if nums[i] < min_val:
                min_val = nums[i]
                min_ind = i
            elif nums[i] > max_val:
                max_val = nums[i]
                max_ind = i
        if max_ind < min_ind:
            min_ind, max_ind = max_ind, min_ind
        return min(
            max_ind + 1, len(nums) - min_ind, min_ind + 1 + len(nums) - max_ind
        )
