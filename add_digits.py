# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.


class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num = sum([int(n) for n in list(str(num))])
        return num
