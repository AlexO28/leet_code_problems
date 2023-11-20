# Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
# Implement the Solution class:
# Solution(int[] nums) Initializes the object with the array nums.
# int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.


import random


class Solution:

    def __init__(self, nums: List[int]):
        self.num_dict = {}
        for j in range(len(nums)):
            if nums[j] in self.num_dict.keys():
                self.num_dict[nums[j]].append(j)
            else:
                self.num_dict[nums[j]] = [j]

    def pick(self, target: int) -> int:
        arr = self.num_dict[target]
        if len(arr) == 1:
            return arr[0]
        return arr[int(random.randint(0, len(arr)-1))]
 
