# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.


from itertools import combinations


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        arr = list(range(len(nums)))
        res = [[]]
        for j in range(1, len(nums) + 1):
            comb_iter = combinations(arr, j)
            for comb in comb_iter:
                temp_arr = []
                for ind in comb:
                    temp_arr.append(nums[ind])
                temp_arr.sort()
                if temp_arr not in res:
                    res.append(temp_arr)
        return res
