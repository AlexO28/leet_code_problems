# Given a non-negative integer num, return true if num can be expressed as the sum of any non-negative integer and its reverse, or false otherwise.
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num == 0:
            return True
        for j in range(1, num):
            if num == j + int(str(j)[::-1]):
                return True
        return False 
