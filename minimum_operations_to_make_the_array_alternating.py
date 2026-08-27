# You are given a 0-indexed array nums consisting of n positive integers.
# The array nums is called alternating if:
# nums[i - 2] == nums[i], where 2 <= i <= n - 1.
# nums[i - 1] != nums[i], where 1 <= i <= n - 1.
# In one operation, you can choose an index i and change nums[i] into any positive integer.
# Return the minimum number of operations required to make the array alternating.
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            if nums[0] == nums[1]:
                return 1
            else:
                return 0
        freq_dict_odd = {}
        freq_dict_even = {}
        for i in range(len(nums)):
            if i % 2 == 0:
                if nums[i] in freq_dict_even:
                    freq_dict_even[nums[i]] += 1
                else:
                    freq_dict_even[nums[i]] = 1
            else:
                if nums[i] in freq_dict_odd:
                    freq_dict_odd[nums[i]] += 1
                else:
                    freq_dict_odd[nums[i]] = 1
        sorted_freq_dict_odd = dict(
            sorted(freq_dict_odd.items(), key=lambda item: item[1], reverse=True)
        )
        sorted_freq_dict_even = dict(
            sorted(freq_dict_even.items(), key=lambda item: item[1], reverse=True)
        )
        sorted_freq_dict_odd_keys = list(sorted_freq_dict_odd.keys())
        sorted_freq_dict_even_keys = list(sorted_freq_dict_even.keys())
        sorted_freq_dict_odd_values = list(sorted_freq_dict_odd.values())
        sorted_freq_dict_even_values = list(sorted_freq_dict_even.values())
        if sorted_freq_dict_odd_keys[0] != sorted_freq_dict_even_keys[0]:
            return (
                sum(sorted_freq_dict_odd_values)
                - sorted_freq_dict_odd_values[0]
                + sum(sorted_freq_dict_even_values)
                - sorted_freq_dict_even_values[0]
            )
        elif (len(sorted_freq_dict_odd_keys) > 1) and (
            (len(sorted_freq_dict_even_keys) > 1)
        ):
            return min(
                sum(sorted_freq_dict_odd_values)
                - sorted_freq_dict_odd_values[1]
                + sum(sorted_freq_dict_even_values)
                - sorted_freq_dict_even_values[0],
                sum(sorted_freq_dict_odd_values)
                - sorted_freq_dict_odd_values[0]
                + sum(sorted_freq_dict_even_values)
                - sorted_freq_dict_even_values[1],
            )
        elif (len(sorted_freq_dict_odd_keys) == 1) and (
            (len(sorted_freq_dict_even_keys) > 1)
        ):
            return (
                sum(sorted_freq_dict_odd_values)
                - sorted_freq_dict_odd_values[0]
                + sum(sorted_freq_dict_even_values)
                - sorted_freq_dict_even_values[1]
            )
        elif (len(sorted_freq_dict_odd_keys) > 1) and (
            (len(sorted_freq_dict_even_keys) == 1)
        ):
            return (
                sum(sorted_freq_dict_odd_values)
                - sorted_freq_dict_odd_values[1]
                + sum(sorted_freq_dict_even_values)
                - sorted_freq_dict_even_values[0]
            )
        else:
            return min(
                sum(sorted_freq_dict_odd_values), sum(sorted_freq_dict_even_values)
            )
