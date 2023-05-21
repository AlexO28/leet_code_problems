# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        found = False
        for j in range(len(digits)):
            if digits[len(digits)-1-j] != 9:
                found = True
                break
        if found:
            digits[len(digits)-1-j] += 1
            if j > 0:
                for k in range(j):
                    digits[len(digits)-1-k] = 0
            return digits
        else:
            return [1] + [0]*len(digits)
