# You are given an array of positive integers nums.
# You need to select a subset of nums which satisfies the following condition:
# You can place the selected elements in a 0-indexed array such that it follows the pattern: [x, x2, x4, ..., xk/2, xk, xk/2, ..., x4, x2, x] (Note that k can be be any non-negative power of 2). For example, [2, 4, 16, 4, 2] and [3, 9, 3] follow the pattern while [2, 4, 8, 4, 2] does not.
# Return the maximum number of elements in a subset that satisfies these conditions.
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        max_length = 1
        for val in num_dict:
            if val == 1:
                charact = num_dict[val]
                if charact % 2 == 0:
                    charact -= 1
                if charact > 1:
                    max_length = max(max_length, charact)
            else:
                x = val
                cur_length = 0
                while True:
                    if x not in num_dict:
                        break
                    else:
                        cur_length += 1
                        if num_dict[x] == 1:
                            break
                        x *= x
                max_length = max(max_length, 2 * cur_length - 1)
        return max_length
