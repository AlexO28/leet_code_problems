# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
# Return true if a and b are alike. Otherwise, return false.
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        VOWELS = "aeiouAEIOU"
        count = 0
        half_len = len(s) // 2
        for i in range(half_len):
            if s[i] in VOWELS:
                count += 1
        for i in range(half_len, len(s)):
            if s[i] in VOWELS:
                count -= 1
        return count == 0
