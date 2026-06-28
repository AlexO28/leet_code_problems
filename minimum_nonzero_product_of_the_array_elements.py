# You are given a positive integer p. Consider an array nums (1-indexed) that consists of the integers in the inclusive range [1, 2p - 1] in their binary representations. You are allowed to do the following operation any number of times:
# Choose two elements x and y from nums.
# Choose a bit in x and swap it with its corresponding bit in y. Corresponding bit refers to the bit that is in the same position in the other integer.
# Find the minimum non-zero product of nums after performing the above operation any number of times. Return this product modulo 109 + 7.
# Note: The answer should be the minimum product before the modulo operation is done.
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 1000000007
        num = 2**p
        return (num - 1) * pow(num - 2, num // 2 - 1, MOD) % MOD
