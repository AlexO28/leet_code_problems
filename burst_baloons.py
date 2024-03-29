# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
# Return the maximum coins you can collect by bursting the balloons wisely.


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums = [1] + nums + [1]
        dp = [[0]*len(nums) for i in range(len(nums))]
        for gap in range(2, len(nums)):
            for i in range(len(nums) - gap):
                j = i + gap
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j])
        return dp[0][len(nums) - 1]
