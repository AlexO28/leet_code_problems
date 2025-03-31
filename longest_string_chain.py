# You are given an array of words where each word consists of lowercase English letters.
# wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.
# Return the length of the longest possible word chain with words chosen from the given list of words.
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        res = 0
        dp = {}
        for current_word in words:
            for j in range(len(current_word)):
                previous_word = current_word[:j] + current_word[(j+1):]
                if previous_word not in dp:
                    dp[previous_word] = 0
                if current_word in dp:
                    dp[current_word] = max(dp[current_word], dp[previous_word] + 1)
                else:
                    dp[current_word] = dp[previous_word] + 1
                res = max(res, dp[current_word])
        return res
