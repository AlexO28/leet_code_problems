# Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.
# For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
# Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.
# Since the answer may be very large, return it modulo 109 + 7.
from typing import List


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        self.kMod = 1000000007
        self.comb = []
        self.generate(len(nums) + 1)
        return self.ways(nums) - 1

    def generate(self, numRows):
        for i in range(numRows):
            self.comb.append([1] * (i + 1))
        for i in range(2, numRows):
            for j in range(1, len(self.comb[i]) - 1):
                self.comb[i][j] = (
                    self.comb[i - 1][j - 1] + self.comb[i - 1][j]
                ) % self.kMod

    def ways(self, nums):
        if len(nums) <= 2:
            return 1
        left = []
        right = []
        for i in range(1, len(nums)):
            if nums[i] < nums[0]:
                left.append(nums[i])
            else:
                right.append(nums[i])
        res = self.comb[len(nums) - 1][len(left)]
        res = (res * self.ways(left)) % self.kMod
        res = (res * self.ways(right)) % self.kMod
        return res
