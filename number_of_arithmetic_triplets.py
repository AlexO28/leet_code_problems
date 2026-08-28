# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.
from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        num_dict = {}
        for j in range(len(nums)):
            if nums[j] in num_dict:
                num_dict[nums[j]].append(j)
            else:
                num_dict[nums[j]] = [j]
        res = 0
        for i in range(len(nums)):
            num1 = nums[i] - diff
            num2 = nums[i] + diff
            if (num1 in num_dict) and (num2 in num_dict):
                res += len(num_dict[num1]) * len(num_dict[num2])
        return res
