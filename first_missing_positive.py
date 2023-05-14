# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        marks = [False]*100000
        for num in nums:
            if (num <= 100000) and (num > 0):
                marks[num-1] = True
        for j in range(len(nums)):
            if marks[j] == False:
                return j+1
        return len(nums) + 1
