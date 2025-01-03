# Given two strings s and t, each of which represents a non-negative rational number, return true if and only if they represent the same number. The strings may use parentheses to denote the repeating part of the rational number.
# A rational number can be represented using up to three parts: <IntegerPart>, <NonRepeatingPart>, and a <RepeatingPart>. The number will be represented in one of the following three ways:
# <IntegerPart>
# <IntegerPart><.><NonRepeatingPart>
# <IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)>
# The repeating portion of a decimal expansion is conventionally denoted within a pair of round brackets.
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        return abs(self.convert(s) - self.convert(t)) < 0.000000001

    def convert(self, num):
        try:
            i = num.index("(")
            non_repeating = num[:i]
            repeating = num[(i+1):(len(num)-1)]
            return float(non_repeating) + float(repeating)/(10**len(repeating)-1)/(10**(i-num.index('.')-1))
        except:
            return float(num)
