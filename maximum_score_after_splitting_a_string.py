# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
class Solution:
    def maxScore(self, s: str) -> int:
        ones = len([elem for elem in s if elem == "1"])
        if s[0] == "0":
            max_score = 1 + ones
            zeros = 1
        else:
            max_score = ones - 1
            zeros = 0
            ones -= 1
        if len(s) == 2:
            return max_score
        for j in range(1, len(s)-1):
            if s[j] == "0":
                zeros += 1
                max_score = max(max_score, zeros + ones)
            else:
                ones -= 1
                max_score = max(max_score, zeros + ones)
        return max_score
