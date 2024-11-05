# You are given a 0-indexed binary string s having an even length.
# A string is beautiful if it's possible to partition it into one or more substrings such that:
# Each substring has an even length.
# Each substring contains only 1's or only 0's.
# You can change any character in s to 0 or 1.
# Return the minimum number of changes required to make the string s beautiful.
class Solution:
    def minChanges(self, s: str) -> int:
        number_of_changes = 0
        for j in range(1, len(s), 2):
            if s[j] != s[j-1]:
                number_of_changes += 1
        return number_of_changes
