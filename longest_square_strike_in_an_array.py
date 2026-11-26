# You are given an integer array nums. A subsequence of nums is called a square streak if:
# The length of the subsequence is at least 2, and
# after sorting the subsequence, each element (except the first element) is the square of the previous number.
# Return the length of the longest square streak in nums, or return -1 if there is no square streak.
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        nums = set(nums)
        max_strike = 1
        for num in nums:
            cur_strike = 1
            candidate = num
            while cur_strike < 6:
                candidate *= candidate
                if candidate in nums:
                    cur_strike += 1
                else:
                    break
                max_strike = max(max_strike, cur_strike)
        if max_strike == 1:
            return -1
        else:
            return max_strike
