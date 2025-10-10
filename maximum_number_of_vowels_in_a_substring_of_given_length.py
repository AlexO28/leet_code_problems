# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_vowels = 0
        for elem in s[:k]:
            if elem in vowels:
                max_vowels += 1
        if len(s) == k:
            return max_vowels
        else:
            cur_vowels = max_vowels
            for j in range(1, len(s) + 1 - k):
                if s[j - 1] in vowels:
                    cur_vowels -= 1
                if s[j + k - 1] in vowels:
                    cur_vowels += 1
                max_vowels = max(max_vowels, cur_vowels)
            return max_vowels
