# Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.
from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) == 1:
            return 1
        sorted_list = SortedList()
        max_size = 0
        start = 0
        for end in range(len(nums)):
            sorted_list.add(nums[end])
            while sorted_list[-1] - sorted_list[0] > limit:
                sorted_list.remove(nums[start])
                start += 1
            max_size = max(max_size, end-start+1)
        return max_size
