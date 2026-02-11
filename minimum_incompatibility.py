# You are given an integer array nums​​​ and an integer k. You are asked to distribute this array into k subsets of equal size such that there are no two equal elements in the same subset.
# A subset's incompatibility is the difference between the maximum and minimum elements in that array.
# Return the minimum possible sum of incompatibilities of the k subsets after distributing the array optimally, or return -1 if it is not possible.
# A subset is a group integers that appear in the array with no particular order.
from math import inf
from typing import List


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        m = len(nums) // k
        g = [-1] * (1 << len(nums))
        for i in range(1, 1 << len(nums)):
            if i.bit_count() != m:
                continue
            s = set()
            mi = 20
            mx = 0
            for j, x in enumerate(nums):
                if i >> j & 1:
                    if x in s:
                        break
                    s.add(x)
                    mi = min(mi, x)
                    mx = max(mx, x)
            if len(s) == m:
                g[i] = mx - mi
        f = [inf] * (1 << len(nums))
        f[0] = 0
        for i in range(1 << len(nums)):
            if f[i] == inf:
                continue
            s = set()
            mask = 0
            for j, x in enumerate(nums):
                if (i >> j & 1) == 0 and x not in s:
                    s.add(x)
                    mask |= 1 << j
            if len(s) < m:
                continue
            j = mask
            while j:
                if g[j] != -1:
                    f[i | j] = min(f[i | j], f[i] + g[j])
                j = (j - 1) & mask
        return f[-1] if f[-1] != inf else -1
