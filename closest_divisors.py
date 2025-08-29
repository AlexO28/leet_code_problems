# Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.
# Return the two integers in any order.
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        if num == 1:
            return [1, 2]
        num_1 = num + 1
        num_2 = num + 2
        max_num = int(num_2**0.5)
        for x in range(max_num, 0, -1):
            main_part_2, remainder_2 = divmod(num_2, x)
            if remainder_2 == 0:
                return [x, main_part_2]
            main_part_1, remainder_1 = divmod(num_1, x)
            if remainder_1 == 0:
                return [x, main_part_1]
