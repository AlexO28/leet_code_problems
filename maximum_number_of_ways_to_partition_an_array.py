# You are given a 0-indexed integer array nums of length n. The number of ways to partition nums is the number of pivot indices that satisfy both conditions:
# 1 <= pivot < n
# nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] + ... + nums[n - 1]
# You are also given an integer k. You can choose to change the value of one element of nums to k, or to leave the array unchanged.
# Return the maximum possible number of ways to partition nums to satisfy both conditions after changing at most one element.
from typing import List
from collections import defaultdict


class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        s = [nums[0]] * len(nums)
        right = defaultdict(int)
        for i in range(1, len(nums)):
            s[i] = s[i - 1] + nums[i]
            right[s[i - 1]] += 1
        ans = 0
        main_part, remainder = divmod(s[-1], 2)
        if remainder == 0:
            ans = right[main_part]
        left = defaultdict(int)
        for v, x in zip(s, nums):
            d = k - x
            main_part, remainder = divmod(s[-1] + d, 2)
            if remainder == 0:
                t = left[main_part] + right[(s[-1] - d) // 2]
                if ans < t:
                    ans = t
            left[v] += 1
            right[v] -= 1
        return ans
