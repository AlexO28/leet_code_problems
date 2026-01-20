# You are given an array nums consisting of n prime integers.
# You need to construct an array ans of length n, such that, for each index i, the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i], i.e. ans[i] OR (ans[i] + 1) == nums[i].
# Additionally, you must minimize each value of ans[i] in the resulting array.
# If it is not possible to find such a value for ans[i] that satisfies the condition, then set ans[i] = -1.
from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        arr = []
        for j in range(len(nums)):
            found = False
            for k in range(1, 1001):
                if k | (k + 1) == nums[j]:
                    found = True
                    break
            if found:
                arr.append(k)
            else:
                arr.append(-1)
        return arr
