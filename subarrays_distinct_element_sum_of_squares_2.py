# You are given a 0-indexed integer array nums.
# The distinct count of a subarray of nums is defined as:
# Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
# Return the sum of the squares of distinct counts of all subarrays of nums.
# Since the answer may be very large, return it modulo 109 + 7.
# A subarray is a contiguous non-empty sequence of elements within an array.
from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        self.n = len(nums) + 1
        self.tree1 = [0] * self.n
        self.tree2 = [0] * self.n
        max_val = max(nums)
        last = [0] * (max_val + 1)
        res = 0
        cur = 0
        for i in range(1, self.n):
            x = nums[i - 1]
            j = last[x]
            cur += 2 * (self.__query(i) - self.__query(j)) + (i - j)
            res += cur
            self.__update(j + 1, 1)
            self.__update(i + 1, -1)
            last[x] = i
        return res % 1000000007


    def __query(self, index):
        res = 0
        p = index + 1
        while index > 0:
            res += p * self.tree1[index] - self.tree2[index]
            index -= self.__lowbit(index)
        return res


    def __update(self, index, x):
        v = index * x
        while index < self.n:
            self.tree1[index] += x
            self.tree2[index] += v
            index += self.__lowbit(index)
        

    def __lowbit(self, index):
        return index & (-index)
