# Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.
# An integer y is a power of three if there exists an integer x such that y == 3x.
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        powers = [
            43046721,
            14348907,
            4782969,
            1594323,
            531441,
            177147,
            59049,
            19683,
            6561,
            2187,
            729,
            243,
            81,
            27,
            9,
            3,
            1,
        ]
        for power in powers:
            delta = n - power
            if delta == 0:
                return True
            elif delta > 0:
                n = delta
        return False
