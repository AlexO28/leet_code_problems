# Given an integer n represented as a string, return the smallest good base of n.
# We call k >= 2 a good base of n, if all digits of n base k are 1's.
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        for term_count in range(63, 1, -1):
            left = 2
            right = num - 1
            while left < right:
                mid = (left + right) // 2
                if self.calculate_sum(mid, term_count) >= num:
                    right = mid
                else:
                    left = mid + 1
            if self.calculate_sum(left, term_count) == num:
                return str(left)
        return str(num - 1)

    def calculate_sum(self, base, term_count):
        power_product = 1
        sum_product = 1
        for i in range(term_count):
            power_product *= base
            sum_product += power_product
        return sum_product
        
