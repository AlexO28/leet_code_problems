# You are given an array nums consisting of positive integers.
# Starting with score = 0, apply the following algorithm:
# Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
# Add the value of the chosen integer to score.
# Mark the chosen element and its two adjacent elements if they exist.
# Repeat until all the array elements are marked.
# Return the score you get after applying the above algorithm.
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        marks = [0]*len(nums)
        num_dict = {i: nums[i] for i in range(len(nums))}
        num_dict = {k: v for k, v in sorted(num_dict.items(), key=lambda item: item[1])}
        score = 0
        for key in num_dict:
            if marks[key] == 0:
                marks[key] = 1
                score += num_dict[key]
                if key > 0:
                    marks[key-1] = 1
                if key < len(nums)-1:
                    marks[key+1] = 1
        return score
