# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        pos1 = 0
        pos2 = 0
        res = []
        remainder = 0
        num1 = list(num1)
        num2 = list(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        while (pos1 < len(num1)) or (pos2 < len(num2)):
            if pos1 == len(num1):
                val1 = 0
            else:
                val1 = int(num1[pos1])
                pos1 += 1
            if pos2 == len(num2):
                val2 = 0
            else:
                val2 = int(num2[pos2])
                pos2 += 1
            remainder, temp = divmod(val1 + val2 + remainder, 10)
            res.append(str(temp))
        if remainder != 0:
            res.append(str(remainder))
        return ''.join(res[::-1])
