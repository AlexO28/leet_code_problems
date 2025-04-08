# You are given an integer array nums. You need to ensure that the elements in the array are distinct. To achieve this, you can perform the following operation any number of times:
# Remove 3 elements from the beginning of the array. If the array has fewer than 3 elements, remove all remaining elements.
# Note that an empty array is considered to have distinct elements. Return the minimum number of operations needed to make the elements in the array distinct.
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        number_of_operations = 0
        j = 0
        while True:
            if j >= len(nums):
                break
            if len(nums[j:]) == len(list(set(nums[j:]))):
                break
            j += 3
            number_of_operations += 1
        return number_of_operations
