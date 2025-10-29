# You are given a positive number n.
# Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits
class Solution:
    def smallestNumber(self, n: int) -> int:
        return int("1" * len("{0:b}".format(n)), 2)
