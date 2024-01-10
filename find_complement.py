# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
# Given an integer num, return its complement.
class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:]
        res = []
        for elem in num:
            if elem == "1":
                res.append("0")
            else:
                res.append("1")
        return int("".join(res), 2)
