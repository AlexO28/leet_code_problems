# Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.
# Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sum1 = 0
        sum2 = 0
        sum3 = 0
        max_sum1 = 0
        max_sum1_2 = 0
        max_index1 = 0
        max_indices1_2 = []
        max_sum = 0
        result = []
        for i in range(k * 2, len(nums)):
            sum1 += nums[i - k * 2]
            sum2 += nums[i - k]
            sum3 += nums[i]
            if i >= k * 3 - 1:
                if sum1 > max_sum1:
                    max_sum1 = sum1
                    max_index1 = i - k * 3 + 1
                if max_sum1 + sum2 > max_sum1_2:
                    max_sum1_2 = max_sum1 + sum2
                    max_indices1_2 = [max_index1, i - k * 2 + 1]
                if max_sum1_2 + sum3 > max_sum:
                    max_sum = max_sum1_2 + sum3
                    result = [max_indices1_2[0], max_indices1_2[1], i - k + 1]
                sum1 -= nums[i - k * 3 + 1]
                sum2 -= nums[i - k * 2 + 1]
                sum3 -= nums[i - k + 1]
        return result
