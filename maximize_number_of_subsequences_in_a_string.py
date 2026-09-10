# You are given a 0-indexed string text and another 0-indexed string pattern of length 2, both of which consist of only lowercase English letters.
# You can add either pattern[0] or pattern[1] anywhere in text exactly once. Note that the character can be added even at the beginning or at the end of text.
# Return the maximum number of times pattern can occur as a subsequence of the modified text.
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        if pattern[0] == pattern[1]:
            return self.find_number_of_subsequences_equal(pattern[0] + text, pattern)
        return max(
            self.find_number_of_subsequences(pattern[0] + text, pattern),
            self.find_number_of_subsequences((text + pattern[1])[::-1], pattern[::-1]),
        )

    def find_number_of_subsequences(self, text, pattern):
        num_start = 0
        res = 0
        for elem in text:
            if elem == pattern[0]:
                num_start += 1
            elif elem == pattern[1]:
                res += num_start
        return res

    def find_number_of_subsequences_equal(self, text, pattern):
        if pattern[0] == pattern[1]:
            num_start = 0
            for elem in text:
                if elem == pattern[0]:
                    num_start += 1
            return num_start * (num_start - 1) // 2
