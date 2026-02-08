# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.
from collections import Counter
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq_dict = Counter(nums)
        main_part = k // 2
        res = 0
        for num in nums:
            if num <= main_part:
                if freq_dict[num] > 0:
                    freq_dict[num] -= 1
                else:
                    continue
                num_complementary = k - num
                if freq_dict[num_complementary] > 0:
                    freq_dict[num_complementary] -= 1
                else:
                    continue
                res += 1
        return res
