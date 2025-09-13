# You are given a string s consisting of lowercase English letters ('a' to 'z').
# Your task is to:
# Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
# Find the consonant (all other letters excluding vowels) with the maximum frequency.
# Return the sum of the two frequencies.
# Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.
# The frequency of a letter x is the number of times it occurs in the string.
class Solution:
    def maxFreqSum(self, s: str) -> int:
        VOWELS = "aeiou"
        freq_dict = {}
        for elem in s:
            if elem in freq_dict:
                freq_dict[elem] += 1
            else:
                freq_dict[elem] = 1
        freq_1 = 0
        freq_2 = 0
        for vowel in VOWELS:
            if vowel in freq_dict:
                freq_1 = max(freq_1, freq_dict[vowel])
        for key in freq_dict:
            if key not in VOWELS:
                freq_2 = max(freq_2, freq_dict[key])
        return freq_1 + freq_2
