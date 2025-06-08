# You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.
# A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.
# Return the minimum length of the substring that can be replaced with any other string of the same length to make s balanced. If s is already balanced, return 0.
class Solution:
    def balancedString(self, s: str) -> int:
        freq_dict = {"Q": 0, "W": 0, "E": 0, "R": 0}
        for elem in s:
            freq_dict[elem] += 1
        target = len(s) // 4
        nevyazka = sum(abs(freq_dict[key] - target) for key in freq_dict)
        if nevyazka == 0:
            return 0
        min_len = len(s)
        start_index = 0
        for i, char in enumerate(s):
            freq_dict[char] -= 1
            while start_index <= i and all(
                count <= target for count in freq_dict.values()
            ):
                min_len = min(min_len, i - start_index + 1)
                freq_dict[s[start_index]] += 1
                start_index += 1
        return min_len
