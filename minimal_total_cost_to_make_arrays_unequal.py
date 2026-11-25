# You are given two 0-indexed integer arrays nums1 and nums2, of equal length n.
# In one operation, you can swap the values of any two indices of nums1. The cost of this operation is the sum of the indices.
# Find the minimum total cost of performing the given operation any number of times such that nums1[i] != nums2[i] for all 0 <= i <= n - 1 after performing all the operations.
# Return the minimum total cost such that nums1 and nums2 satisfy the above condition. In case it is not possible, return -1.
from collections import Counter


class Solution:
    def minimumTotalCost(self, nums1: list[int], nums2: list[int]) -> int:
        res = 0
        same = 0
        cnt = Counter()
        for i, (a, b) in enumerate(zip(nums1, nums2)):
            if a == b:
                same += 1
                res += i
                cnt[a] += 1
        m = 0
        lead = 0
        for k, v in cnt.items():
            delta = 2 * v - same
            if delta > 0:
                m = delta
                lead = k
                break
        for i, (a, b) in enumerate(zip(nums1, nums2)):
            if m and a != b and a != lead and b != lead:
                res += i
                m -= 1
        if m > 0:
            return -1
        else:
            return res
