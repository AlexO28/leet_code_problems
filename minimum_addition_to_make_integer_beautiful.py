# You are given two positive integers n and target.
# An integer is considered beautiful if the sum of its digits is less than or equal to target.
# Return the minimum non-negative integer x such that n + x is beautiful. The input will be generated such that it is always possible to make n beautiful.
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        x = 0
        while True:
            nn = n + x
            if self.find(nn) <= target:
                break
            else:
                y = nn
                p = 10
                while True:
                    main_part, remainder = divmod(y, 10)
                    if remainder > 0:
                        break
                    else:
                        y = main_part
                        p *= 10
                x = (y // 10 + 1) * p - n
        return x

    def find(self, x):
        y = 0
        while x:
            x, remainder = divmod(x, 10)
            y += remainder
        return y
