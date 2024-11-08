# Given an array of digits which is sorted in non-decreasing order. You can write numbers using each digits[i] as many times as we want. For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.
# Return the number of positive integers that can be generated that are less than or equal to a given integer n.
from functools import cache


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        length_of_n = 0
        self.a = [0] * 12
        self.digit_set = {int(d) for d in digits}
        while n:
            length_of_n += 1
            self.a[length_of_n] = n % 10
            n //= 10
        return self.search(length_of_n, True, True)

    @cache
    def search(self, position, is_leading, is_limit):
            if position <= 0:
                return int(not is_leading)
            if is_limit:
                upper_bound = self.a[position]
            else:
                upper_bound = 9
            count = 0
            for i in range(upper_bound + 1):
                if i == 0 and is_leading:
                    count += self.search(position - 1, is_leading, is_limit and i == upper_bound)
                elif i in self.digit_set:
                    count += self.search(position - 1, False, is_limit and i == upper_bound)
            return count
