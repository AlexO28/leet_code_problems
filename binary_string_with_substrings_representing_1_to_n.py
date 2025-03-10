# Given a binary string s and a positive integer n, return true if the binary representation of all the integers in the range [1, n] are substrings of s, or false otherwise.
# A substring is a contiguous sequence of characters within a string.
class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1, n+1):
            if "{0:b}".format(i) not in s:
                return False
        return True
