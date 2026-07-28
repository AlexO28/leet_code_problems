# You are given a palindromic string s.
# Return the lexicographically smallest palindromic permutation of s.
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq_dict = {}
        for elem in s:
            if elem in freq_dict:
                freq_dict[elem] += 1
            else:
                freq_dict[elem] = 1
        keys = list(freq_dict.keys())
        keys.sort()
        left_part = []
        middle_part = ""
        for key in keys:
            main_part, remainder = divmod(freq_dict[key], 2)
            left_part.extend(key * main_part)
            if remainder == 1:
                middle_part = key
        return "".join(left_part) + middle_part + "".join(left_part[::-1])
