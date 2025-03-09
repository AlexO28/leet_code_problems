# Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.
# Return the length of n. If there is no such n, return -1.
# Note: n may not fit in a 64-bit signed integer.
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1:
            return 1
        else:
            remainder = 1
            for length in range(1, k+1):
                if remainder == 0:
                    return length
                else:
                    remainder = (remainder * 10 + 1) % k
            return -1
