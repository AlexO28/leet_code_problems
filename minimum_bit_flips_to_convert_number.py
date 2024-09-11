# A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.
# Given two integers start and goal, return the minimum number of bit flips to convert start to goal.
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = str(bin(start))[2:]
        goal = str(bin(goal))[2:]
        res = 0
        min_val = len(goal)
        if len(goal) > len(start):
            min_val = len(start)
            for j in range(len(goal)-len(start)):
                if goal[j] == "1":
                    res += 1
        elif len(start) > len(goal):
            for j in range(len(start)-len(goal)):
                if start[j] == "1":
                    res += 1
        for j in range(min_val):
            if start[len(start)-j-1] != goal[len(goal)-j-1]:
                res += 1
        return res
