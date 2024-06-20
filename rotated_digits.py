# An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.
# A number is valid if each digit remains a digit after rotation. For example:
# 0, 1, and 8 rotate to themselves,
# 2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
# 6 and 9 rotate to each other, and
# the rest of the numbers do not rotate to any other number and become invalid.
# Given an integer n, return the number of good integers in the range [1, n].
class Solution:
    def rotatedDigits(self, n: int) -> int:
        counter = 0
        for num in range(1, n+1):
            if self.isGood(num):
                counter += 1
        return counter

    def isGood(self, n):
        num = list(str(n))
        new_num = []
        for digit in num:
            if digit in ["0", "1", "8"]:
                new_num.append(digit)
            elif digit == "2":
                new_num.append("5")
            elif digit == "5":
                new_num.append("2")
            elif digit == "6":
                new_num.append("9")
            elif digit == "9":
                new_num.append("6")
            else:
                return False
        new_n = int("".join(new_num))
        return new_n != n
