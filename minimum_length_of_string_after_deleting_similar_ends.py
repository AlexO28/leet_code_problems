# Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:
# Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
# Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
# The prefix and the suffix should not intersect at any index.
# The characters from the prefix and suffix must be the same.
# Delete both the prefix and the suffix.
# Return the minimum length of s after performing the above operation any number of times (possibly zero times).
class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        while (i < j) and (s[i] == s[j]):
            while (i + 1 < j) and (s[i] == s[i + 1]):
                i += 1
            while (i < j - 1) and (s[j - 1] == s[j]):
                j -= 1
            i += 1
            j -= 1
        return max(0, j - i + 1)
