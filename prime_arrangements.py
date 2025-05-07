# Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)
# (Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)
# Since the answer may be large, return the answer modulo 10^9 + 7.
from math import factorial


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        number_of_primes = self.count_primes(n)
        return (factorial(number_of_primes) * factorial(n - number_of_primes)) % (10 ** 9 + 7)

    def count_primes(self, n):
        count = 0
        is_prime = [True] * (n + 1)
        for i in range(2, n + 1):
            if is_prime[i]:
                count += 1
                for j in range(2 * i, n + 1, i):
                    is_prime[j] = False
        return count
