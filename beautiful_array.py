# An array nums of length n is beautiful if:
# nums is a permutation of the integers in the range [1, n].
# For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].
# Given the integer n, return any beautiful array nums of length n. There will be at least one valid answer for the given n.
from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        return self.generateArray(n)

    def generateArray(self, n):
        if n == 1:
            return [1]
        else:
            left_half = self.generateArray((n + 1) // 2)
            right_half = self.generateArray(n // 2)
            return [2 * element - 1 for element in left_half] + [2 * element for element in right_half]
