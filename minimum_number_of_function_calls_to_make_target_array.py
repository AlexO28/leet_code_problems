# You are given an integer array nums. You have an integer array arr of the same length with all values set to 0 initially. You also have the following modify function:
# You want to use the modify function to convert arr to nums using the minimum number of calls.
# Return the minimum number of function calls to make nums from arr.
# The test cases are generated so that the answer fits in a 32-bit signed integer.
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        number_of_operations = 0
        indices = [j for j in range(len(nums)) if nums[j] > 0]
        while len(indices) > 0:
            new_indices = []
            for index in indices:
                if nums[index] == 1:
                    number_of_operations += 1
                else:
                    if nums[index] % 2 == 1:
                        nums[index] -= 1
                        number_of_operations += 1
                    new_indices.append(index)
            indices = new_indices
            if len(indices) > 0:
                for index in indices:
                    nums[index] /= 2
                number_of_operations += 1
        return number_of_operations
