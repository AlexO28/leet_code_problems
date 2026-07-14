# An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.
# Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 > 0:
            return []
        freq_dict = {}
        for num in changed:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        keys = list(freq_dict.keys())
        keys.sort()
        res = []
        for key in keys:
            if freq_dict[key] == 0:
                continue
            if key == 0:
                main_part, remainder = divmod(freq_dict[key], 2)
                if (remainder > 0):
                    return []
                else:
                    res.extend([0] * (main_part))
            else:
                new_key = 2 * key
                if (new_key not in freq_dict):
                    return []
                freq_dict[new_key] -= freq_dict[key]
                if freq_dict[new_key] < 0:
                    return []
                res.extend([key] * freq_dict[key])
        return res
