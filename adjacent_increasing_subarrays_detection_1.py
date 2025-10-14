# Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:
# Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
# The subarrays must be adjacent, meaning b = a + k.
# Return true if it is possible to find two such subarrays, and false otherwise.
from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if (len(nums) == 2) or (k == 1):
            return True
        else:
            for i in range(len(nums) - 2 * k + 1):
                found = False
                upper = i + k
                for j in range(i + 1, upper):
                    if nums[j] <= nums[j - 1]:
                        found = True
                        break
                if found:
                    continue
                for j in range(upper + 1, upper + k):
                    if nums[j] <= nums[j - 1]:
                        found = True
                        break
                if not found:
                    return True
            return False
