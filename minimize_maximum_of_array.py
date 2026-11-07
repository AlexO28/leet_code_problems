# You are given a 0-indexed array nums comprising of n non-negative integers.
# In one operation, you must:
# Choose an integer i such that 1 <= i < n and nums[i] > 0.
# Decrease nums[i] by 1.
# Increase nums[i - 1] by 1.
# Return the minimum possible value of the maximum integer of nums after performing any number of operations.
class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        left = 0
        right = max(nums)
        while left < right:
            mid = (left + right) >> 1
            if self.check(mid, nums):
                right = mid
            else:
                left = mid + 1
        return left

    def check(self, mx, nums):
        d = 0
        for x in nums[:0:-1]:
            d = max(0, d + x - mx)
        return nums[0] + d <= mx
