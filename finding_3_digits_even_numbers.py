# You are given an integer array digits, where each element is a digit. The array may contain duplicates.
# You need to find all the unique integers that follow the given requirements:
# The integer consists of the concatenation of three elements from digits in any arbitrary order.
# The integer does not have leading zeros.
# The integer is even.
# Return a sorted array of the unique integers.
from typing import List
from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq_dict = Counter(digits)
        res = []
        for num in range(100, 1000, 2):
            num_dict = Counter([int(elem) for elem in list(str(num))])
            not_found = True
            for elem in num_dict:
                if elem in freq_dict:
                    if freq_dict[elem] < num_dict[elem]:
                        not_found = False
                        break
                else:
                    not_found = False
                    break
            if not_found:
                res.append(num)
        return res
