# You are given a string s consisting of digits. Perform the following operation repeatedly until the string has exactly two digits:
# For each pair of consecutive digits in s, starting from the first digit, calculate a new digit as the sum of the two digits modulo 10.
# Replace s with the sequence of newly calculated digits, maintaining the order in which they are computed.
# Return true if the final two digits in s are the same; otherwise, return false.
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(s)
        s = [int(elem) for elem in s]
        while len(s) > 2:
            new_line = []
            for i in range(1, len(s)):
                new_line.append((s[i - 1] + s[i]) % 10)
            s = new_line.copy()
        return s[-1] == s[-2]
