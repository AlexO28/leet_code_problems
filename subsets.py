# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.


from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for j in range(1, len(nums) + 1):
            iter_comb = combinations(nums, j)
            for comb in iter_comb:
                res.append(comb)
        return res
