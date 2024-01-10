# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
class Solution:
    def frequencySort(self, s: str) -> str:
        freq_dict = {}
        for elem in s:
            if elem in freq_dict:
                freq_dict[elem] += 1
            else:
                freq_dict[elem] = 1
        freq_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        res = []
        for key, val in freq_dict:
            res.extend([key]*val)
        return "".join(res)
