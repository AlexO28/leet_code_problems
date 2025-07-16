# You are given an integer array nums.
# A subsequence sub of nums with length x is called valid if it satisfies:
# (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
# Return the length of the longest valid subsequence of nums.
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        number_of_even = 0
        number_of_odd = 0
        for num in nums:
            if num % 2 == 0:
                number_of_even += 1
            else:
                number_of_odd += 1
        if number_of_even == 0:
            return number_of_odd
        if number_of_odd == 0:
            return number_of_even
        number_of_even_odd = 0
        search_even = True
        for num in nums:
            if num % 2 == 0:
                if search_even:
                    search_even = False
                    number_of_even_odd += 1
            else:
                if not search_even:
                    search_even = True
                    number_of_even_odd += 1
        number_of_odd_even = 0
        search_odd = True
        for num in nums:
            if num % 2 == 0:
                if not search_odd:
                    search_odd = True
                    number_of_odd_even += 1
            else:
                if search_odd:
                    search_odd = False
                    number_of_odd_even += 1
        return max(
            number_of_even, number_of_odd, number_of_even_odd, number_of_odd_even
        )
