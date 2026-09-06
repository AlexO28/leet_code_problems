# Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) such that:
# 0 <= i < j <= n - 1 and
# nums[i] * nums[j] is divisible by k.
import math
from typing import List
from collections import Counter


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        gcd_counts = Counter(math.gcd(num, k) for num in nums)
        ans = 0
        gcd_list = list(gcd_counts.keys())
        for i in range(len(gcd_list)):
            gcd1 = gcd_list[i]
            count1 = gcd_counts[gcd1]
            if (gcd1 * gcd1) % k == 0:
                ans += (count1 * (count1 - 1)) // 2
            for j in range(i + 1, len(gcd_list)):
                gcd2 = gcd_list[j]
                count2 = gcd_counts[gcd2]
                if (gcd1 * gcd2) % k == 0:
                    ans += count1 * count2
        return ans
