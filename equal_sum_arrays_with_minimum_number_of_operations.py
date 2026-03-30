# You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.
# In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.
# Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.
from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1)
        s2 = sum(nums2)
        if s1 == s2:
            return 0
        if s1 > s2:
            s1, s2 = s2, s1
            nums1, nums2 = nums2, nums1
        cnt = Counter([6 - v for v in nums1] + [v - 1 for v in nums2])
        d = s2 - s1
        ans = 0
        for i in range(5, 0, -1):
            while cnt[i] and d > 0:
                d -= i
                cnt[i] -= 1
                ans += 1
        if d <= 0:
            return ans
        else:
            return -1
