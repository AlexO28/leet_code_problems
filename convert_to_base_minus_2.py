# Given an integer n, return a binary string representing its representation in base -2.
# Note that the returned string should not have leading zeros unless the string is "0".
class Solution:
    def baseNeg2(self, n: int) -> str:
        power_of_neg_2 = 1
        result_digits = []
        while n > 0:
            if n % 2 > 0:
                result_digits.append("1")
                n -= power_of_neg_2
            else:
                result_digits.append("0")
            n //= 2
            power_of_neg_2 *= -1
        if len(result_digits) > 0:
            return "".join(reversed(result_digits))
        else:
            return "0"
