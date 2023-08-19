# Reverse bits of a given 32 bits unsigned integer.


class Solution:
    def reverseBits(self, n: int) -> int:
        str = "{0:b}".format(n)[::-1]
        if len(str) < 32:
            str += "0"*(32-len(str))
        return int(str, 2)
