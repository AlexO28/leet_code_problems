# You are given an integer array target. You have an integer array initial of the same size as target with all elements initially zeros.
# In one operation you can choose any subarray from initial and increment each value by one.
# Return the minimum number of operations to form a target array from initial.
# The test cases are generated so that the answer fits in a 32-bit integer.
from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        total_operations = target[0]
        for i in range(1, len(target)):
            previous_height = target[i - 1]
            current_height = target[i]
            height_increase = max(0, current_height - previous_height)
            total_operations += height_increase
        return total_operations
