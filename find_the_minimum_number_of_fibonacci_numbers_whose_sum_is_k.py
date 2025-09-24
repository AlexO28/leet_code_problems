# Given an integer k, return the minimum number of Fibonacci numbers whose sum is equal to k. The same Fibonacci number can be used multiple times.
# The Fibonacci numbers are defined as:
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2 for n > 2.
# It is guaranteed that for the given constraints we can always find such Fibonacci numbers that sum up to k.
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib_numbers = [1, 1]
        while True:
            num = fib_numbers[-1] + fib_numbers[-2]
            if num > k:
                break
            else:
                fib_numbers.append(num)
        res = 0
        pos = len(fib_numbers) - 1
        while True:
            delta = k - fib_numbers[pos]
            if delta > 0:
                res += 1
                k = delta
            elif delta == 0:
                return res + 1
            else:
                while pos > 0:
                    if k - fib_numbers[pos] >= 0:
                        break
                    else:
                        pos -= 1
