# You are given an integer array nums.
# A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].
# The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.
# Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.
from typing import List
from math import inf


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        min_dist = inf
        num_dict = {}
        for i in range(len(nums)):
            if nums[i] in num_dict:
                num_dict[nums[i]].append(i)
            else:
                num_dict[nums[i]] = [i]
        for num in num_dict:
            if len(num_dict[num]) >= 3:
                num_dict[num].sort()
                for i in range(len(num_dict[num]) - 2):
                    min_dist = min(
                        min_dist, 2 * (num_dict[num][i + 2] - num_dict[num][i])
                    )
        if min_dist < inf:
            return min_dist
        else:
            return -1
