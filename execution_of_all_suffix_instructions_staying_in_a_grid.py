# There is an n x n grid, with the top-left cell at (0, 0) and the bottom-right cell at (n - 1, n - 1). You are given the integer n and an integer array startPos where startPos = [startrow, startcol] indicates that a robot is initially at cell (startrow, startcol).
# You are also given a 0-indexed string s of length m where s[i] is the ith instruction for the robot: 'L' (move left), 'R' (move right), 'U' (move up), and 'D' (move down).
# The robot can begin executing from any ith instruction in s. It executes the instructions one by one towards the end of s but it stops if either of these conditions is met:
# The next instruction will move the robot off the grid.
# There are no more instructions left to execute.
# Return an array answer of length m where answer[i] is the number of instructions the robot can execute if the robot begins executing from the ith instruction in s.
from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        res = []
        for i in range(len(s)):
            x = startPos[1]
            y = startPos[0]
            number_of_instructions = 0
            for j in range(i, len(s)):
                if s[j] == "L":
                    if (x > 0):
                        x -= 1
                        number_of_instructions += 1
                    else:
                        break
                elif s[j] == "R":
                    if (x < n - 1):
                        x += 1
                        number_of_instructions += 1
                    else:
                        break
                elif s[j] == "U":
                    if (y > 0):
                        y -= 1
                        number_of_instructions += 1
                    else:
                        break
                elif s[j] == 'D':
                    if (y < n - 1):
                        y += 1
                        number_of_instructions += 1
                    else:
                        break
            res.append(number_of_instructions)
        return res
