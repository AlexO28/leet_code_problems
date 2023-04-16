# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

import numpy as np


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        else:
            return self.myPowRecursive(x, n)
    def myPowRecursive(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1/x
        elif abs(n) % 2 == 0:
            return self.myPowRecursive(x, n/2) ** 2
        else:
            n_min = np.floor(abs(n)/2) * np.sign(n)
            if n > 0:
                return x * self.myPowRecursive(x, n_min) ** 2
            else:
                return (self.myPowRecursive(x, n_min) ** 2)/x
