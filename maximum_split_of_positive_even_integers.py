# You are given an integer finalSum. Split it into a sum of a maximum number of unique positive even integers.
# For example, given finalSum = 12, the following splits are valid (unique positive even integers summing up to finalSum): (12), (2 + 10), (2 + 4 + 6), and (4 + 8). Among them, (2 + 4 + 6) contains the maximum number of integers. Note that finalSum cannot be split into (2 + 2 + 4 + 4) as all the numbers should be unique.
# Return a list of integers that represent a valid split containing a maximum number of integers. If no valid split exists for finalSum, return an empty list. You may return the integers in any order.
from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        visited = set()
        final_sum = finalSum
        for num in range(2, final_sum, 2):
            new_final_sum = final_sum - num
            if (new_final_sum <= 0):
                break
            if (new_final_sum != num) and (num not in visited) and (new_final_sum not in visited):
                visited.add(num)
                final_sum = new_final_sum
            else:
                break
        delta = finalSum - sum(visited)
        if delta > 0:
            visited.add(delta)
        return list(visited)
