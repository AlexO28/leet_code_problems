# You are given an array of n integers, nums, where there are at most 50 unique values in the array. You are also given an array of m customer order quantities, quantity, where quantity[i] is the amount of integers the ith customer ordered. Determine if it is possible to distribute nums such that:
# The ith customer gets exactly quantity[i] integers,
# The integers the ith customer gets are all equal, and
# Every customer is satisfied.
# Return true if it is possible to distribute nums according to the above conditions.
from collections import Counter
from typing import List


class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        s = [0] * (1 << len(quantity))
        for i in range(1, 1 << len(quantity)):
            for j in range(len(quantity)):
                if i >> j & 1:
                    s[i] = s[i ^ (1 << j)] + quantity[j]
                    break
        cnt = Counter(nums)
        arr = list(cnt.values())
        f = [[False] * (1 << len(quantity)) for _ in range(len(arr))]
        for i in range(len(arr)):
            f[i][0] = True
        for i, x in enumerate(arr):
            for j in range(1, 1 << len(quantity)):
                if i and f[i - 1][j]:
                    f[i][j] = True
                    continue
                k = j
                while k:
                    if i == 0:
                        ok1 = j == k
                    else:
                        ok1 = f[i - 1][j ^ k]
                    ok2 = s[k] <= x
                    if ok1 and ok2:
                        f[i][j] = True
                        break
                    k = (k - 1) & j
        return f[-1][-1]
