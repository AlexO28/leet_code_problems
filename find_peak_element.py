# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return nums.index(max(nums))
