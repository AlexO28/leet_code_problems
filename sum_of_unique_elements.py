# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] = 2
            else:
                freq_dict[num] = 1
        return sum([elem for elem in freq_dict if freq_dict[elem] == 1])
