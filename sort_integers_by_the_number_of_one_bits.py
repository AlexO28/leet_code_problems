# You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.
# Return the array after sorting it.
import numpy as np


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr_2 = []
        for elem in arr:
            elem_list = list(bin(elem))
            arr_2.append(len([el for el in elem_list if el == "1"]) + (1 + elem)/(10 ** 5))
        return np.array(arr)[np.argsort(arr_2)]
 
