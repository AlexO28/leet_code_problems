# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = "aeiouAEIOU"
        line_vowels = []
        vowels_pos = []
        for j in range(len(s)):
            if s[j] in VOWELS:
                vowels_pos.append(j)
                line_vowels.append(s[j])
        if len(line_vowels) <= 1:
            return s
        s = list(s)
        ind = len(line_vowels) - 1
        for j in vowels_pos:
            s[j] = line_vowels[ind]
            ind -= 1
        return ''.join(s)
                
