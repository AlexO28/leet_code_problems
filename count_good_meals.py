# A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.
# You can pick any two different foods to make a good meal.
# Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 109 + 7.
# Note that items with different indices are considered different even if they have the same deliciousness value.
from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        POWERS = [
            1,
            2,
            4,
            8,
            16,
            32,
            64,
            128,
            256,
            512,
            1024,
            2048,
            4096,
            8192,
            16384,
            32768,
            65536,
            131072,
            262144,
            524288,
            1048576,
            2097152,
        ]
        MOD = 1000000007
        freq_dict = {}
        for num in deliciousness:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        res = 0
        for num in freq_dict.keys():
            for power in POWERS:
                delta = power - num
                if delta >= num:
                    if delta in freq_dict:
                        if delta > num:
                            res += freq_dict[num] * freq_dict[delta]
                        else:
                            res += (freq_dict[num] - 1) * freq_dict[num] // 2
                        res = res % MOD
        return res
