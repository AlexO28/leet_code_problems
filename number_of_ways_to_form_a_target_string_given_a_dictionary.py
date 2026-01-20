# You are given a list of strings of the same length words and a string target.
# Your task is to form target using the given words under the following rules:
# target should be formed from left to right.
# To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
# Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
# Repeat the process until you form the string target.
# Notice that you can use multiple characters from the same string in words provided the conditions above are met.
# Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.
from typing import List
from functools import cache


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        self.target = target
        self.words = words
        self.cnt = [[0] * 26 for i in range(len(self.words[0]))]
        for w in self.words:
            for j, c in enumerate(w):
                self.cnt[j][ord(c) - ord("a")] += 1
        self.MOD = 1000000007
        return self.search(0, 0)

    @cache
    def search(self, i, j):
        if i >= len(self.target):
            return 1
        elif j >= len(self.words[0]):
            return 0
        else:
            ans = (
                self.search(i + 1, j + 1) * self.cnt[j][ord(self.target[i]) - ord("a")]
            )
            ans = (ans + self.search(i, j + 1)) % self.MOD
            return ans
