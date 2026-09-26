# You are given a 0-indexed integer array nums. In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.
# Return the number of steps performed until nums becomes a non-decreasing array.
class Solution:
    def totalSteps(self, nums: list[int]) -> int:
        stack = []
        dp = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                dp[i] = max(dp[i] + 1, dp[stack.pop()])
            stack.append(i)
        return max(dp)
