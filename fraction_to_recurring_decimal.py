# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        res = []
        if ((numerator > 0) & (denominator < 0) |
            (numerator < 0) & (denominator > 0)):
            res.append('-')
        numerator = abs(numerator)
        denominator = abs(denominator)
        res.append(str(numerator // denominator))
        numerator %= denominator
        if numerator == 0:
            return ''.join(res)
        res.append('.')
        temp_dict = {}
        while numerator != 0:
            temp_dict[numerator] = len(res)
            numerator *= 10
            res.append(str(numerator // denominator))
            numerator %= denominator
            if numerator in temp_dict.keys():
                id = temp_dict[numerator]
                res.insert(id, '(')
                res.append(')')
                break
        return ''.join(res)
