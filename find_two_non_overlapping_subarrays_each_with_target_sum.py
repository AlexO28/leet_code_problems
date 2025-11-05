# You are given an array of integers arr and an integer target.
# You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.
# Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.
from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        cumsum_to_index = {0: 0}
        cumulative_sum = 0
        min_length = [float("inf")] * (len(arr) + 1)
        min_total_length = float("inf")
        for j in range(len(arr)):
            cumulative_sum += arr[j]
            min_length[j + 1] = min_length[j]
            required_sum = cumulative_sum - target
            if required_sum in cumsum_to_index:
                start_index = cumsum_to_index[required_sum]
                current_subarray_length = j - start_index + 1
                min_length[j + 1] = min(min_length[j + 1], current_subarray_length)
                combined_length = min_length[start_index] + current_subarray_length
                min_total_length = min(min_total_length, combined_length)
            cumsum_to_index[cumulative_sum] = j + 1
        if min_total_length > len(arr):
            return -1
        else:
            return min_total_length
