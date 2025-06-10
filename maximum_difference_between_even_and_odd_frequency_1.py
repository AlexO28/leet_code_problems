# You are given a string s consisting of lowercase English letters.
# Your task is to find the maximum difference diff = a1 - a2 between the frequency of characters a1 and a2 in the string such that:
# a1 has an odd frequency in the string.
# a2 has an even frequency in the string.
# Return this maximum difference.
class Solution:
    def maxDifference(self, s: str) -> int:
        freq_dict = {}
        for elem in s:
            if elem in freq_dict:
                freq_dict[elem] += 1
            else:
                freq_dict[elem] = 1
        odds = []
        evens = []
        for val in freq_dict.values():
            if val % 2 == 0:
                evens.append(val)
            else:
                odds.append(val)
        return max(odds) - min(evens)
