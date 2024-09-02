# Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        n *= 2
        count = 0
        k = 1
        while k*(k+1) <= n:
            main_part, remainder = divmod(n, k)
            if (remainder == 0) and ((main_part + 1 - k) % 2 == 0):
                count += 1
            k += 1
        return count
