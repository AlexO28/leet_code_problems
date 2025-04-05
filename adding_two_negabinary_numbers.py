# Given two numbers arr1 and arr2 in base -2, return the result of adding them together.
# Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.  For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array, format is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.
# Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.
from typing import List


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        pointer_arr1 = len(arr1) - 1
        pointer_arr2 = len(arr2) - 1
        carry = 0
        result = []
        while pointer_arr1 >= 0 or pointer_arr2 >= 0 or carry != 0:
            if pointer_arr1 < 0:
                digit_arr1 = 0
            else:
                digit_arr1 = arr1[pointer_arr1]
            if pointer_arr2 < 0:
                digit_arr2 = 0
            else:
                digit_arr2 = arr2[pointer_arr2]
            digit_sum = digit_arr1 + digit_arr2 + carry
            carry = 0 
            if digit_sum >= 2:
                digit_sum -= 2
                carry -= 1
            elif digit_sum == -1:
                digit_sum = 1
                carry += 1          
            result.append(digit_sum)
            pointer_arr1, pointer_arr2 = pointer_arr1 - 1, pointer_arr2 - 1
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return result[::-1]
