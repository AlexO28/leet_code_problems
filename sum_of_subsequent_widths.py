# The width of a sequence is the difference between the maximum and minimum elements in the sequence.
# Given an array of integers nums, return the sum of the widths of all the non-empty subsequences of nums. Since the answer may be very large, return it modulo 109 + 7.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        nums.sort()
        result = 0
        power = 1
        for j in range(len(nums)):
            result = (result + (nums[j] - nums[-j-1]) * power) % mod
            power = (2 * power) % mod
        return result
