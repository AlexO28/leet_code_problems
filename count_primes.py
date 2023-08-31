# Given an integer n, return the number of prime numbers that are strictly less than n.


class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 0
        dict = {}
        for j in range(2, n):
            dict[j] = False
        for num in range(2, n):
            if 2*num > n:
                break
            if not dict[num]:    
                for j in range(2*num, n, num):
                    if not dict[j]:
                        dict[j] = True
        count = 0
        for j in range(2, n):
            if not dict[j]:
                count += 1
        return count
