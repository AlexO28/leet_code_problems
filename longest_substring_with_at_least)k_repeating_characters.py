# Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.
# if no such substring exists, return 0.


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        number_of_unique_characters = len(set(list(s)))
        for j in range(1, number_of_unique_characters+1):
            freq_dict_new = {}
            start = 0
            end = 0
            number_of_unique = 0
            number_of_frequent = 0
            while end < len(s):
                if number_of_unique <= j:
                    if s[end] not in freq_dict_new.keys():
                        number_of_unique += 1
                        freq_dict_new[s[end]] = 1
                    else:
                        freq_dict_new[s[end]] += 1
                    if freq_dict_new[s[end]] == k:
                        number_of_frequent += 1
                    end += 1
                else:
                    if freq_dict_new[s[start]] == k:
                        number_of_frequent -= 1
                    if freq_dict_new[s[start]] == 1:
                        del freq_dict_new[s[start]]
                        number_of_unique -= 1
                    else:
                        freq_dict_new[s[start]] -= 1
                    start += 1
                if (number_of_unique == j) and (number_of_frequent == j):
                    res = max(res, end-start)
        return res
