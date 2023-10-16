# A super ugly number is a positive integer whose prime factors are in the array primes.
# Given an integer n and an array of integers primes, return the nth super ugly number.


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1
        ugly_numbers = [1]*n
        pointers = [0]*len(primes)
        next_values = [0]*len(primes)
        for i in range(1, n):
            for j in range(len(pointers)):
                next_values[j] = ugly_numbers[pointers[j]]*primes[j]
            ugly_numbers[i] = min(next_values)
            for j in range(len(pointers)):
                if next_values[j] == ugly_numbers[i]:
                    pointers[j] += 1
        return ugly_numbers[-1]
