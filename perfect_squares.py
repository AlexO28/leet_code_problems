# Given an integer n, return the least number of perfect square numbers that sum to n.


class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        for j in range(1, 1 + int(n ** 0.5)):
            squares.append(j * j)
        for i in range(len(squares)):
            if n == squares[i]:
                return 1
        for i in range(len(squares)):
            for j in range(i, len(squares)):
                if n == squares[i] + squares[j]:
                    return 2
        for i in range(len(squares)):
            for j in range(i, len(squares)):
                for k in range(j, len(squares)):
                    if n == squares[i] + squares[j] + squares[k]:
                        return 3
        return 4
        
