# Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.
# Implement the Solution class:
# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns it.
# int[] shuffle() Returns a random shuffling of the array.
import numpy as np


class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums
        

    def reset(self) -> List[int]:
        return self.arr

    def shuffle(self) -> List[int]:
        return np.random.permutation(self.arr)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
