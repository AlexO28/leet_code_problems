# Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.
# All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.
class Solution:
    def toHex(self, num: int) -> str:
        if num >= 0:
            return format(num, 'x')
        else:
            return format(1 + num + 4294967295, 'x')
