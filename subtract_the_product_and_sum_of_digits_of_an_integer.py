# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
from math import prod


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_list = [int(elem) for elem in list(str(n))]
        return prod(n_list) - sum(n_list)
