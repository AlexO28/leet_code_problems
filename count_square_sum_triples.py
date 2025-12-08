# A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.
# Given an integer n, return the number of square triples such that 1 <= a, b, c <= n
class Solution:
    def countTriples(self, n: int) -> int:
        squares = []
        for i in range(1, n + 1):
            squares.append(i**2)
        squares = set(squares)
        res = 0
        for a in squares:
            for b in squares:
                if a + b in squares:
                    res += 1
        return res
