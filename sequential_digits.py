# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        numbers = [str(i) for i in range(1, 10)]
        for j in range(len(str(high)) - 1):
            new_numbers = []
            for number_array in numbers:
                new_numbers.append(number_array)
                val = int(number_array[-1]) 
                if val < 9:
                    new_numbers.append(number_array + str(val + 1))
            numbers = list(set(new_numbers))
        res = []
        for number_array in numbers:
            val = int(number_array)
            if low <= val <= high:
                res.append(val)
        return sorted(res)
