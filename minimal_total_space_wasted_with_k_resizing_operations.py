# You are currently designing a dynamic array. You are given a 0-indexed integer array nums, where nums[i] is the number of elements that will be in the array at time i. In addition, you are given an integer k, the maximum number of times you can resize the array (to any size).
# The size of the array at time t, sizet, must be at least nums[t] because there needs to be enough space in the array to hold all the elements. The space wasted at time t is defined as sizet - nums[t], and the total space wasted is the sum of the space wasted across every time t where 0 <= t < nums.length.
# Return the minimum total space wasted if you can resize the array at most k times.
# Note: The array can have any size at the start and does not count towards the number of resizing operations.
from typing import List
from math import inf


class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        k += 2
        g = [[0] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums)):
            s = 0
            maxVal = 0
            for j in range(i, len(nums)):
                s += nums[j]
                maxVal = max(maxVal, nums[j])
                g[i][j] = maxVal * (j - i + 1) - s
        f = [[inf] * k for _ in range(len(nums) + 1)]
        f[0][0] = 0
        for i in range(1, len(nums) + 1):
            for j in range(1, k):
                for h in range(i):
                    f[i][j] = min(f[i][j], f[h][j - 1] + g[h][i - 1])
        return f[-1][-1]
