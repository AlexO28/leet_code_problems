# You are given an array apple of size n and an array capacity of size m.
# There are n packs where the ith pack contains apple[i] apples. There are m boxes as well, and the ith box has a capacity of capacity[i] apples.
# Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes.
# Note that, apples from the same pack can be distributed into different boxes.
from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        number_of_apples = sum(apple)
        capacity.sort(reverse=True)
        summa = 0
        j = 0
        while summa < number_of_apples:
            summa += capacity[j]
            j += 1
        return j
