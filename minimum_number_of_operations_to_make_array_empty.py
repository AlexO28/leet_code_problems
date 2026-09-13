# You are given a 0-indexed array nums consisting of positive integers.
# There are two types of operations that you can apply on the array any number of times:
# Choose two elements with equal values and delete them from the array.
# Choose three elements with equal values and delete them from the array.
# Return the minimum number of operations required to make the array empty, or -1 if it is not possible
from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq_dict = Counter(nums)
        number_of_rounds = 0
        for freq in freq_dict.values():
            if freq == 1:
                return -1
            elif freq == 4:
                number_of_rounds += 2
            else:
                main_part, remainder = divmod(freq, 3)
                if remainder == 0:
                    number_of_rounds += main_part
                elif remainder == 2:
                    number_of_rounds += main_part + 1
                else:
                    main_part, remainder = divmod(freq - 2, 3)
                    number_of_rounds += main_part + 2
        return number_of_rounds
