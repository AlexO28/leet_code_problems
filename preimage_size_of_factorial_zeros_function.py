# Let f(x) be the number of zeroes at the end of x!. Recall that x! = 1 * 2 * 3 * ... * x and by convention, 0! = 1.
# Given an integer k, return the number of non-negative integers x have the property that f(x) = k.
from bisect import bisect_left


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        return self.left_boundary_of_k(k+1) - self.left_boundary_of_k(k)

    def left_boundary_of_k(self, k):
        return bisect_left(range(5*k), k, key=self.calculate_number_of_zeros)

    def calculate_number_of_zeros(self, x):
        if x == 0:
            return 0
        else:
            return x//5 + self.calculate_number_of_zeros(x//5)
