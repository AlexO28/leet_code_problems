# You are given an integer array nums and an integer k.
# An array is considered balanced if the value of its maximum element is at most k times the minimum element.
# You may remove any number of elements from nums​​​​​​​ without making it empty.
# Return the minimum number of elements to remove so that the remaining array is balanced.
from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        j = 0
        min_val = len(nums) - 1
        for i in range(len(nums) - 1):
            j = max(i, j)
            while (j < len(nums)) and (nums[j] <= k * nums[i]):
                j += 1
            min_val = min(min_val, len(nums) - (j - i))
        return min_val
