# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.
# Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for j in range(len(nums)):
            if (not stack) or (nums[stack[-1]] > nums[j]):
                stack.append(j)
        max_ramp = 0
        for j in range(len(nums)-1, -1, -1):
            while stack and (nums[stack[-1]] <= nums[j]):
                max_ramp = max(max_ramp, j-stack.pop())
            if not stack:
                break 
        return max_ramp
