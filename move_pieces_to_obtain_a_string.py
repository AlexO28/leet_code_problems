# You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:
# The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
# The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
# Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i = 0
        j = 0
        while True:
            while i < len(start) and start[i] == '_':
                i += 1
            while j < len(target) and target[j] == '_':
                j += 1
            if i >= len(start) and j >= len(target):
                return True
            if i >= len(start) or j >= len(target) or start[i] != target[j]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            i += 1
            j += 1
