# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_sum_end = nums[0]
        min_sum_end = nums[0]
        max_subarray_sum = nums[0]
        min_subarray_sum = nums[0]
        for num in nums[1:]:
            max_sum_end = num + max(max_sum_end, 0)
            min_sum_end = num + min(min_sum_end, 0)
            max_subarray_sum = max(max_subarray_sum, max_sum_end)
            min_subarray_sum = min(min_subarray_sum, min_sum_end)
        if max_subarray_sum <= 0:
            return max_subarray_sum
        else:
            return max(max_subarray_sum, sum(nums)-min_subarray_sum)
