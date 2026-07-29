# You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n to minimize the absolute difference of the sums of the arrays. To partition nums, put each element of nums into one of the two arrays.
# Return the minimum possible absolute difference.
from typing import List
from collections import defaultdict
from math import inf


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        f = defaultdict(set)
        g = defaultdict(set)
        for i in range(2**n):
            s = 0
            cnt = 0
            s1 = 0
            cnt1 = 0
            for j in range(n):
                if (i & (1 << j)) != 0:
                    s += nums[j]
                    cnt += 1
                    s1 += nums[n + j]
                    cnt1 += 1
                else:
                    s -= nums[j]
                    s1 -= nums[n + j]
            f[cnt].add(s)
            g[cnt1].add(s1)
        ans = inf
        for i in range(n + 1):
            fi = sorted(list(f[i]))
            gi = sorted(list(g[n - i]))
            for a in fi:
                left = 0
                right = len(gi) - 1
                b = -a
                while left < right:
                    mid = (left + right) // 2
                    if gi[mid] >= b:
                        right = mid
                    else:
                        left = mid + 1
                ans = min(ans, abs(a + gi[left]))
                if left > 0:
                    ans = min(ans, abs(a + gi[left - 1]))
        return ans
