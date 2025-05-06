# You are given a string text. You should split it to k substrings (subtext1, subtext2, ..., subtextk) such that:
# subtexti is a non-empty string.
# The concatenation of all the substrings is equal to text (i.e., subtext1 + subtext2 + ... + subtextk == text).
# subtexti == subtextk - i + 1 for all valid values of i (i.e., 1 <= i <= k).
# Return the largest possible value of k.
class Solution:
    def longestDecomposition(self, text: str) -> int:
        count = 0
        start = 0
        end = len(text) - 1
        while start <= end:
            match_length = 1
            found_match = False
            while start + match_length - 1 < end - match_length + 1:
                if text[start:start + match_length] == text[end - match_length + 1:end + 1]:
                    count += 2
                    start += match_length
                    end -= match_length
                    found_match = True
                    break
                match_length += 1
            if not found_match:
                count += 1
                break
        return count
