# A swap is defined as taking two distinct positions in an array and swapping the values in them.
# A circular array is defined as an array where we consider the first element and the last element to be adjacent.
# Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            if num == 1:
                total += 1
        if total <= 1:
            return 0
        nums.extend(nums)
        num_zeros = 0
        for i in range(total):
            if nums[i] == 0:
                num_zeros += 1
        min_zeros = num_zeros
        for i in range(1, len(nums) - total - 1):
            if nums[i - 1] == 0:
                num_zeros -= 1
            if nums[i + total - 1] == 0:
                num_zeros += 1
            min_zeros = min(min_zeros, num_zeros)
        return min_zeros
