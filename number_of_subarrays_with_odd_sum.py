# Given an array of integers arr, return the number of subarrays with an odd sum.
# Since the answer can be very large, return it modulo 109 + 7.
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        count = [1, 0]
        answer = 0
        prefix_sum = 0
        for num in arr:
            prefix_sum += num
            answer = (answer + count[prefix_sum % 2 ^ 1]) % (10 ** 9 + 7)
            count[prefix_sum % 2] += 1
        return answer
