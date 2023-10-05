# Given an integer n, return true if it is a power of three. Otherwise, return false.

import numpy as np


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        num = round(np.log(n)/np.log(3), 10)
        return num == int(num)
