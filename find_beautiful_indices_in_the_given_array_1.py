# You are given a 0-indexed string s, a string a, a string b, and an integer k.
# An index i is beautiful if:
# 0 <= i <= s.length - a.length
# s[i..(i + a.length - 1)] == a
# There exists an index j such that:
# 0 <= j <= s.length - b.length
# s[j..(j + b.length - 1)] == b
# |j - i| <= k
# Return the array that contains beautiful indices in sorted order from smallest to largest.
from typing import List
from bisect import bisect_left


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        if (len(a) > len(s)) or (len(b) > len(s)):
            return []
        a_data = []
        for i in range(len(s) - len(a) + 1):
            for j in range(i, i + len(a)):
                if s[j] != a[j - i]:
                    break
            else:
                a_data.append(i)
        b_data = []
        for i in range(len(s) - len(b) + 1):
            for j in range(i, i + len(b)):
                if s[j] != b[j - i]:
                    break
            else:
                b_data.append(i)
        res = []
        if (len(a_data) == 0) or (len(b_data) == 0):
            return []
        for i in a_data:
            ind = bisect_left(b_data, i)
            if ind == 0:
                if abs(b_data[0] - i) <= k:
                    res.append(i)
            elif ind == len(b_data):
                if abs(b_data[-1] - i) <= k:
                    res.append(i)
            else:
                if (abs(b_data[ind - 1] - i) <= k) or (abs(b_data[ind] - i) <= k):
                    res.append(i)
        return res
