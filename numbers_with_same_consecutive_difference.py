# Given two integers n and k, return an array of all the integers of length n where the difference between every two consecutive digits is k. You may return the answer in any order.
# Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.
from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.results = []
        for i in range(1, 10):
            self.search(n-1, k, i)
        return self.results

    def search(self, num_length, k, current_number):
        if num_length == 0:
            self.results.append(current_number)
        else:
            last_digit = current_number % 10
            new_num = current_number * 10 + last_digit
            if last_digit + k <= 9:
                self.search(num_length-1, k, new_num + k)
            if (k != 0) and (last_digit - k >= 0):
                self.search(num_length-1, k, new_num - k)
