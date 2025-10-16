# You are given a 0-indexed integer array nums and an integer value.
# In one operation, you can add or subtract value from any element of nums.
# For example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to make nums = [-1,2,3].
# The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.
# For example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.
# Return the maximum MEX of nums after applying the mentioned operation any number of times.
from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq_dict = {}
        for num in nums:
            num_mod = num % value
            if num_mod in freq_dict:
                freq_dict[num_mod] += 1
            else:
                freq_dict[num_mod] = 1
        num = 0
        while True:
            num_mod = num % value
            if num_mod in freq_dict:
                if freq_dict[num_mod] == 1:
                    del freq_dict[num_mod]
                else:
                    freq_dict[num_mod] -= 1
                num += 1
            else:
                return num
