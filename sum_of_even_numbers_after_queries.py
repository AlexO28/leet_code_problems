# You are given an integer array nums and an array queries where queries[i] = [vali, indexi].
# For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.
# Return an integer array answer where answer[i] is the answer to the ith query.
from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        summa = sum([num for num in nums if num % 2 == 0])
        for query in queries:
            if nums[query[1]] % 2 == 0:
                summa -= nums[query[1]]
            nums[query[1]] += query[0]
            if nums[query[1]] % 2 == 0:
                summa += nums[query[1]]
            res.append(summa)
        return res
