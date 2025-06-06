# Given an array nums of positive integers, return the longest possible length of an array prefix of nums, such that it is possible to remove exactly one element from this prefix so that every number that has appeared in it will have the same number of occurrences.
# If after removing one element there are no remaining elements, it's still considered that every appeared number has the same number of ocurrences (0).
from typing import List
from collections import Counter


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        frequency_counter = Counter()
        frequencies_count = Counter()
        answer = 0
        max_frequency = 0
        for i, num in enumerate(nums, 1):
            if num in frequency_counter:
                frequencies_count[frequency_counter[num]] -= 1
            frequency_counter[num] += 1
            num_frequency = frequency_counter[num]
            max_frequency = max(max_frequency, num_frequency)
            frequencies_count[num_frequency] += 1
            if max_frequency == 1:
                answer = i
            elif frequencies_count[max_frequency] * max_frequency + frequencies_count[max_frequency - 1] * (max_frequency - 1) == i and frequencies_count[max_frequency] == 1:
                answer = i
            elif frequencies_count[max_frequency] * max_frequency + 1 == i and frequencies_count[1] == 1:
                answer = i      
        return answer
