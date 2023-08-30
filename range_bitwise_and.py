# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0:
            return 0
        step = 1
        while left != right:
            left = int(left / 2)
            right = int(right / 2)
            step *= 2
        if left == 0:
            return 0
        return int(left * step)
