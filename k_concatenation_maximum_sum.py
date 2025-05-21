# Given an integer array arr and an integer k, modify the array by repeating it k times.
# For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].
# Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.
# As the answer can be very large, return the answer modulo 109 + 7.
from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        total_sum = 0
        max_prefix = 0
        min_prefix = 0
        max_subarray_sum = 0
        for num in arr:
            total_sum += num
            max_prefix = max(max_prefix, total_sum)
            min_prefix = min(min_prefix, total_sum)
            max_subarray_sum = max(max_subarray_sum, total_sum - min_prefix)
        if k == 1:
            return max_subarray_sum % (10 ** 9 + 7)
        else:
            if total_sum > 0:
                term = max_prefix + total_sum - min_prefix
                return max(max_subarray_sum, term, ((k - 2) * total_sum) + term) % (10 ** 9 + 7)
            else:
                return max(max_subarray_sum, max_prefix + total_sum - min_prefix) % (10 ** 9 + 7)
