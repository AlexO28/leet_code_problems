# Given an integer n, you must transform it into 0 using the following operations any number of times:
# Change the rightmost (0th) bit in the binary representation of n.
# Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
# Return the minimum number of operations to transform n into 0.
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        return self.calculate(n)

    def calculate(self, n):
        if n == 0:
            return 0
        k = 1
        while True:
            new_k = k << 1
            if new_k > n:
                break
            else:
                k = new_k
        return new_k - 1 - self.calculate(k ^ n)
