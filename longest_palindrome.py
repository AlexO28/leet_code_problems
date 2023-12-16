# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_dict = {}
        for elem in s:
            if elem in freq_dict:
                freq_dict[elem] += 1
            else:
                freq_dict[elem] = 1
        tot_len = 0
        found = False
        for elem in freq_dict.keys():
            if freq_dict[elem] % 2 == 0:
                tot_len += freq_dict[elem]
            else:
                found = True
                tot_len += freq_dict[elem] - 1
        if found:
            return tot_len + 1
        else:
            return tot_len
