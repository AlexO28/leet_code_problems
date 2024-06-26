# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = str(bin(n))
        if len(n) == 1:
            return True
        for j in range(1, len(n)):
            if n[j] == n[j-1]:
                return False
        return True
