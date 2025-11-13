# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        main_part, remainder = divmod(high - low + 1, 2)
        if remainder == 0:
            return main_part
        else:
            if low % 2 == 0:
                return main_part
            else:
                return main_part + 1
