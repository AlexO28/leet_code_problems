# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer n, return its complement.
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        num = bin(n)[2:]
        res = []
        for elem in num:
            if elem == "1":
                res.append("0")
            else:
                res.append("1")
        return int("".join(res), 2)
