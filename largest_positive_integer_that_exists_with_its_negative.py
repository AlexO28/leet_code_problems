# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
# Return the positive integer k. If there is no such integer, return -1.
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return -1
        nums.sort(reverse=True)
        for num in nums:
            if num < 0:
                return -1
            elif -num in nums:
                return num
        return -1
