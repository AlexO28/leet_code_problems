# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
# Given an integer n, return true if n is a perfect number, otherwise return false.
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        if num == 2:
            return False
        summa = 1
        for i in range(2, int(num ** 0.5)+1):
            a, b = divmod(num, i)
            if b == 0:
                summa += i
                summa += a
                if summa > num:
                    return False
        return num == summa
        
