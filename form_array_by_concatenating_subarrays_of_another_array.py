# You are given a 2D integer array groups of length n. You are also given an integer array nums.
# You are asked if you can choose n disjoint subarrays from the array nums such that the ith subarray is equal to groups[i] (0-indexed), and if i > 0, the (i-1)th subarray appears before the ith subarray in nums (i.e. the subarrays must be in the same order as groups).
# Return true if you can do this task, and false otherwise.
# Note that the subarrays are disjoint if and only if there is no index k such that nums[k] belongs to more than one subarray. A subarray is a contiguous sequence of elements within an array.
from typing import List


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        start = 0
        for group in groups:
            if len(nums) - start < len(group):
                return False
            ind = start
            found_match = False
            next_ind = start
            while ind < len(nums):
                found = False
                for j in range(len(group)):
                    if ind + j >= len(nums):
                        return False
                    if group[j] != nums[ind + j]:
                        found = True
                        break
                    else:
                        next_ind = ind + j + 1
                if not found:
                    found_match = True
                    break
                ind += 1
            if not found_match:
                return False
            start = next_ind
        return True
