# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        all_squares = {}
        for i in range(int(c ** 0.5)  + 2):
            all_squares[i ** 2] = 1
        for i in all_squares.keys():
            if c - i in all_squares:
                return True
        return False
