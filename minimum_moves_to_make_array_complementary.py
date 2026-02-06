# You are given an integer array nums of even length n and an integer limit. In one move, you can replace any integer from nums with another integer between 1 and limit, inclusive.
# The array nums is complementary if for all indices i (0-indexed), nums[i] + nums[n - 1 - i] equals the same number. For example, the array [1,2,3,4] is complementary because for all indices i, nums[i] + nums[n - 1 - i] = 5.
# Return the minimum number of moves required to make nums complementary.
from itertools import accumulate
from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        d = [0] * (2 * limit + 2)
        for i in range(len(nums) // 2):
            x = nums[i]
            y = nums[-i - 1]
            if x > y:
                x, y = y, x
            d[2] += 2
            x_plus = x + 1
            y_plus = y + 1
            d[x_plus] -= 1
            d[x + y] -= 1
            d[x_plus + y] += 1
            d[y_plus + limit] += 1
        return min(accumulate(d[2:]))
