# Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.
# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.
# Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.
from typing import List
import itertools


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_firstnum = None
        max_secondnum = None
        res = ""
        for permutation in itertools.permutations(arr):
            if permutation[0] > 2:
                continue
            if (permutation[0] == 2) and (permutation[1] > 3):
                continue 
            if permutation[2] > 5:
                continue
            firstnum = int(str(permutation[0]) + str(permutation[1]))
            if (max_firstnum is not None) and (max_firstnum > firstnum):
                continue
            secondnum = int(str(permutation[2]) + str(permutation[3]))
            if (max_secondnum is not None) and (max_firstnum == firstnum) and (max_secondnum >= secondnum):
                continue
            max_firstnum = firstnum
            max_secondnum = secondnum
            res = str(permutation[0]) + str(permutation[1]) + ":" + str(permutation[2]) + str(permutation[3])
        return res
