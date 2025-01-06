# The array-form of an integer num is an array representing its digits in left to right order.
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        if len(num) <= 5:
            new_num = int("".join(str(num[i]) for i in range(len(num)))) + k
            return [int(elem) for elem in list(str(new_num))]
        pos = len(num)-1
        new_num = []
        while k > 0:
            if pos < 0:
                new_num.append(k)
                break
            k, remainder = divmod(num[pos] + k, 10)
            new_num.append(remainder)
            pos -= 1
        while pos >= 0:
            new_num.append(num[pos])
            pos -= 1
        return new_num[::-1]
