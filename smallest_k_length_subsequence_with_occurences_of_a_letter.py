# You are given a string s, an integer k, a letter letter, and an integer repetition.
# Return the lexicographically smallest subsequence of s of length k that has the letter letter appear at least repetition times. The test cases are generated so that the letter appears in s at least repetition times.
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
# A string a is lexicographically smaller than a string b if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        letter_count = 0
        for elem in s:
            if elem == letter:
                letter_count += 1
        res = []
        for i in range(len(s)):
            while (len(res) > 0) and (k - len(res) < len(s) - i) and (res[-1] > s[i]):
                if res[-1] == letter:
                    if letter_count == repetition:
                        break
                    else:
                        repetition += 1
                del res[-1]
            if len(res) == k:
                if s[i] == letter:
                    letter_count -= 1
                continue
            if k - len(res) == repetition:
                if s[i] == letter:
                    res += s[i]
                    repetition -= 1
                    letter_count -= 1
            else:
                res += s[i]
                if s[i] == letter:
                    repetition -= 1
                    letter_count -= 1
        return "".join(res)
