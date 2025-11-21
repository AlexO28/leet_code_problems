# Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:
# The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
# A substring that contains a certain character c must also contain all occurrences of c.
# Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.
# Notice that you can return the substrings in any order.
from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        left = [len(s)] * 26
        right = [0] * 26
        for i in range(len(s)):
            index = ord(s[i]) - ord("a")
            left[index] = min(left[index], i)
            right[index] = i
        res = []
        r = -1
        for i in range(len(s)):
            index_delta = ord(s[i]) - ord("a") 
            if i != left[index_delta]:
                continue
            new_r = right[index_delta]
            j = i + 1
            while j < new_r + 1:
                index_delta = ord(s[j]) - ord("a") 
                if left[index_delta] < i:
                    new_r = len(s)
                    break
                new_r = max(new_r, right[index_delta])
                j = j + 1
            if new_r < len(s) and (i > r or new_r < right[ord(s[r]) - ord("a")]):
                if i > r:
                    res.append(s[i : new_r + 1])
                else:
                    res[-1] = s[i : new_r + 1]
                r = new_r
        return res
