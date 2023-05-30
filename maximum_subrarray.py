# Given an integer array nums, find the subarray with the largest sum, and return its sum.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        localMaxSum = nums[0]
        if len(nums) == 1:
            return maxSum
        for num in nums[1:]:
            localMaxSum = num + max(0, localMaxSum)
            maxSum = max(maxSum, localMaxSum)
        return maxSum
