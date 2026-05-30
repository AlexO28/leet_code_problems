# The minimum absolute difference of an array a is defined as the minimum value of |a[i] - a[j]|, where 0 <= i < j < a.length and a[i] != a[j]. If all elements of a are the same, the minimum absolute difference is -1.
# For example, the minimum absolute difference of the array [5,2,3,7,2] is |2 - 3| = 1. Note that it is not 0 because a[i] and a[j] must be different.
# You are given an integer array nums and the array queries where queries[i] = [li, ri]. For each query i, compute the minimum absolute difference of the subarray nums[li...ri] containing the elements of nums between the 0-based indices li and ri (inclusive).
# Return an array ans where ans[i] is the answer to the ith query.
# A subarray is a contiguous sequence of elements in an array.
from typing import List
from math import inf


class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        pre_sum = [[0] * 101 for i in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            for j in range(1, 101):
                if nums[i - 1] == j:
                    pre_sum[i][j] = pre_sum[i - 1][j] + 1
                else:
                    pre_sum[i][j] = pre_sum[i - 1][j]
        res = []
        for i in range(len(queries)):
            left = queries[i][0]
            right = queries[i][1] + 1
            temp = inf
            last = -1
            for j in range(1, 101):
                if pre_sum[right][j] > pre_sum[left][j]:
                    if last != -1:
                        temp = min(temp, j - last)
                    last = j
            if temp == inf:
                res.append(-1)
            else:
                res.append(temp)
        return res
