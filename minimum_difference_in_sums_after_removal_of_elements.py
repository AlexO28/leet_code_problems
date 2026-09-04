# You are given a 0-indexed integer array nums consisting of 3 * n elements.
# You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:
# The first n elements belonging to the first part and their sum is sumfirst.
# The next n elements belonging to the second part and their sum is sumsecond.
# The difference in sums of the two parts is denoted as sumfirst - sumsecond.
# Return the minimum difference possible between the sums of the two parts after the removal of n elements.
from typing import List
from heapq import heappop, heappush


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        len_plus = len(nums) + 1
        n = len(nums) // 3
        double_n = 2 * n
        s = 0
        pre = [0] * (len_plus)
        q1 = []
        for i, x in enumerate(nums[:double_n], 1):
            s += x
            heappush(q1, -x)
            if len(q1) > n:
                s -= -heappop(q1)
            pre[i] = s
        s = 0
        suf = [0] * (len_plus)
        q2 = []
        for i in range(len(nums), n, -1):
            x = nums[i - 1]
            s += x
            heappush(q2, x)
            if len(q2) > n:
                s -= heappop(q2)
            suf[i] = s
        return min(pre[i] - suf[i + 1] for i in range(n, double_n + 1))
