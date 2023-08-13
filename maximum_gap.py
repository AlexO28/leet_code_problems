# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        max_diff = 0
        for j in range(1, len(nums)):
            max_diff = max(max_diff, nums[j] - nums[j-1]) 
        return max_diff
