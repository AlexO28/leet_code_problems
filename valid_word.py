# A word is considered valid if:
# It contains a minimum of 3 characters.
# It contains only digits (0-9), and English letters (uppercase and lowercase).
# It includes at least one vowel.
# It includes at least one consonant.
# You are given a string word.
# Return true if word is valid, otherwise, return false.
# Notes:
# 'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
# A consonant is an English letter that is not a vowel.
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        digits = set(list("0123456789"))
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        letters = set(list(vowels + consonants))
        vowels = set(list(vowels))
        consonants = set(list(consonants))
        has_vowel = False
        has_consonant = False
        word = word.lower()
        for elem in list(word):
            if (elem not in digits) and (elem not in letters):
                return False
            if not has_vowel:
                if elem in vowels:
                    has_vowel = True
            if not has_consonant:
                if elem in consonants:
                    has_consonant = True
        return has_vowel and has_consonant
