# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
# Return the minimized largest sum of the split.
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = int((left + right)/2)
            if self.is_feasible(mid, nums, k):
                right = mid
            else:
                left = mid + 1
        return left

    def is_feasible(self, max_sum, nums, k):
        current_sum = 0
        splits = 1
        for number in nums:
            current_sum += number
            if current_sum > max_sum:
                current_sum = number
                splits += 1
        return splits <= k
