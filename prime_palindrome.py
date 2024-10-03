# Given an integer n, return the smallest prime palindrome greater than or equal to n.
# An integer is prime if it has exactly two divisors: 1 and itself. Note that 1 is not a prime number.
# For example, 2, 3, 5, 7, 11, and 13 are all primes.
# An integer is a palindrome if it reads the same from left to right as it does from right to left.
# For example, 101 and 12321 are palindromes.
# The test cases are generated so that the answer always exists and is in the range [2, 2 * 108].
class Solution:
    def primePalindrome(self, n: int) -> int:
        max_num_left = 10**7
        max_num_right = 10*max_num_left
        while True:
            if max_num_left <= n <= max_num_right:
                return 100030001
            n_str = str(n)
            if n_str == n_str[::-1]:
                if self.isPrime(n):
                    return n
            n += 1

    def isPrime(self, n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n == 3:
            return True
        for j in range(2, int(n ** 0.5)+1):
            if n % j == 0:
                return False
        return True
