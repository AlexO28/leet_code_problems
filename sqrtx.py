# Implement sqrt function with rounding to the nearest lowest number.


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        next_num = 0
        for j in range(x+1):
            prev_num = next_num
            next_num = j*j
            if x <= next_num:
                break
        if x == next_num:
            return j
        return j - 1
