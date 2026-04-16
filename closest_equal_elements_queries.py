# You are given a circular array nums and an array queries.
# For each query i, you have to find the following:
# The minimum distance between the element at index queries[i] and any other index j in the circular array, where nums[j] == nums[queries[i]]. If no such index exists, the answer for that query should be -1.
# Return an array answer of the same size as queries, where answer[i] represents the result for query i.
from typing import List
from bisect import bisect_left


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        num_dict = {}
        for j in range(len(nums)):
            if nums[j] in num_dict:
                num_dict[nums[j]].append(j)
            else:
                num_dict[nums[j]] = [j]
        for num in num_dict:
            num_dict[num].sort()
        res = []
        for j in queries:
            if len(num_dict[nums[j]]) == 1:
                res.append(-1)
            else:
                ind = bisect_left(num_dict[nums[j]], j)
                res.append(
                    min(
                        self.calculate_circular_distance(
                            num_dict[nums[j]][ind], num_dict[nums[j]][ind - 1], len(nums)
                        ),
                        self.calculate_circular_distance(
                            num_dict[nums[j]][ind],
                            num_dict[nums[j]][(ind + 1) % len(num_dict[nums[j]])],
                            len(nums)
                        ),
                    )
                )
        return res

    def calculate_circular_distance(self, i, j, n):
        return min(abs(i - j), n - abs(i - j))
