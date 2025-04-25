# We are given hours, a list of the number of hours worked per day for a given employee.
# A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.
# A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.
# Return the length of the longest well-performing interval.
from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        hours = [1 if hour > 8 else -1 for hour in hours]
        prefixes = []
        cur_sum = 0
        prefixes = [0]
        for hour in hours:
            cur_sum += hour
            prefixes.append(cur_sum)
        max_interval = 0
        for j in range(1, len(prefixes)):
            for i in range(0, j):
                if prefixes[i] < prefixes[j]:
                    max_interval = max(max_interval, j - i)
                    break
        return max_interval
