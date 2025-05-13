# You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:
# If the character is 'z', replace it with the string "ab".
# Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
# Return the length of the resulting string after exactly t transformations.
# Since the answer may be very large, return it modulo 109 + 7.
from collections import Counter


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        freq_dict = Counter(list(s))
        for i in range(t):
            new_freq_dict = {}
            for elem in freq_dict:
                if elem == "z":
                    if "a" in new_freq_dict:
                        new_freq_dict["a"] += freq_dict["z"]
                    else:
                        new_freq_dict["a"] = freq_dict["z"]
                    if "b" in new_freq_dict:
                        new_freq_dict["b"] += freq_dict["z"]
                    else:
                        new_freq_dict["b"] = freq_dict["z"]
                else:
                    new_letter = chr(ord(elem) + 1)
                    if new_letter in new_freq_dict:
                        new_freq_dict[new_letter] += freq_dict[elem]
                    else:
                        new_freq_dict[new_letter] = freq_dict[elem]
            freq_dict = new_freq_dict
        return sum(freq_dict.values()) % (10 ** 9 + 7)
