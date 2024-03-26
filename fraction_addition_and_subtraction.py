# Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.
# The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.
from math import gcd


class Solution:
    def fractionAddition(self, expression: str) -> str:
        num, den = self.processFraction(expression)
        return str(int(num)) + "/" + str(int(den))

    def processFraction(self, fraction):
        ind = 0
        if (fraction[0] == "-") or (fraction[0] == "+"):
            ind = 1
        found = -1
        for j in range(ind, len(fraction)):
            if (fraction[j] == "+") or (fraction[j] == "-"):
                found = j
                break
        if found < 0:
            return self.reduceFraction(fraction)
        num_1, den_1 = self.reduceFraction(fraction[:j])
        num_2, den_2 = self.processFraction(fraction[j:])
        return self.reduceFraction(str(num_1*den_2 + den_1*num_2) + "/" + str(den_1*den_2))

    def reduceFraction(self, fraction):
        num, den = fraction.split("/")
        num = int(float(num))
        den = int(float(den))
        common = gcd(num, den)
        return num/common, den/common
