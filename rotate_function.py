# You are given an integer array nums of length n.
# Assume arrk to be an array obtained by rotating nums by k positions clock-wise. We define the rotation function F on nums as follow:
# F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1].
# Return the maximum value of F(0), F(1), ..., F(n-1).
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        sum_val = 0
        init_val = 0
        for j in range(len(nums)):
            init_val += j*nums[j]
            sum_val += nums[j]
        max_val = init_val
        for j in range(len(nums)):
            init_val = init_val - sum_val + len(nums)*nums[j]
            max_val = max(max_val, init_val)
        return max_val
