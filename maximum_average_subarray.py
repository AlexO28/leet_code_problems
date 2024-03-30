# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        if len(nums) == k:
            return max_sum/k
        i = 0
        cur_sum = max_sum
        for j in range(k, len(nums)):
            cur_sum += nums[j] - nums[i]
            i += 1
            max_sum = max(max_sum, cur_sum)
        return max_sum/k
