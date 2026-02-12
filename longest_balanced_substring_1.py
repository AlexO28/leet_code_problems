# You are given a string s consisting of lowercase English letters.
# A substring of s is called balanced if all distinct characters in the substring appear the same number of times.
# Return the length of the longest balanced substring of s.
from collections import Counter


class Solution:
    def longestBalanced(self, s: str) -> int:
        if len(s) == 1:
            return 1
        max_len = 1
        for i in range(len(s) - 1):
            freq_dict = {}
            for j in range(i, len(s)):
                cur_len = j - i + 1
                if s[j] in freq_dict:
                    freq_dict[s[j]] += 1
                else:
                    freq_dict[s[j]] = 1
                if cur_len <= max_len:
                    continue
                found = False
                if len(freq_dict) > 1:
                    cur_freq = -1
                    for elem in freq_dict:
                        if cur_freq < 0:
                            cur_freq = freq_dict[elem]
                        else:
                            if cur_freq != freq_dict[elem]:
                                found = True
                                break
                if not found:
                    max_len = max(max_len, cur_len)
        return max_len
