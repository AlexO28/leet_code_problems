# There is a 1 million by 1 million grid on an XY-plane, and the coordinates of each grid square are (x, y).
# We start at the source = [sx, sy] square and want to reach the target = [tx, ty] square. There is also an array of blocked squares, where each blocked[i] = [xi, yi] represents a blocked square with coordinates (xi, yi).
# Each move, we can walk one square north, east, south, or west if the square is not in the array of blocked squares. We are also not allowed to walk outside of the grid.
# Return true if and only if it is possible to reach the target square from the source square through a sequence of valid moves.
from typing import List


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        self.blocked = blocked
        self.blocked = set(map(tuple, self.blocked))
        return self.search(source, target, set()) and self.search(target, source, set())

    def search(self, current, target, seen):
        x, y = current
        if not (0 <= x < 1000000 and 0 <= y < 1000000) or (x, y) in self.blocked or (x, y) in seen:
            return False
        seen.add((x, y))
        if len(seen) > 20000 or current == target:
            return True
        for delta_x, delta_y in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            if self.search([x + delta_x, y + delta_y], target, seen):
                return True
        return False
