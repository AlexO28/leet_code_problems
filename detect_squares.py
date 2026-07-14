# You are given a stream of points on the X-Y plane. Design an algorithm that:
# Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
# Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
# An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.
# Implement the DetectSquares class:
# DetectSquares() Initializes the object with an empty data structure.
# void add(int[] point) Adds a new point point = [x, y] to the data structure.
# int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.
from typing import List


class DetectSquares:

    def __init__(self):
        self.points = {}
        self.slices = {}
        

    def add(self, point: List[int]) -> None:
        code = str(point[0]) + "-" + str(point[1])
        if code in self.points:
            self.points[code] += 1
        else:
            self.points[code] = 1
        if point[0] in self.slices:
            self.slices[point[0]].add(point[1])
        else:
            self.slices[point[0]] = {point[1]}

    def count(self, point: List[int]) -> int:
        res = 0
        if point[0] not in self.slices:
            return 0
        for y in self.slices[point[0]]:
            delta = abs(y - point[1])
            vertex = str(point[0]) + "-" + str(y)
            if delta > 0:
                new_x = point[0] - delta
                vertex_1 = str(new_x) + "-" + str(point[1])
                vertex_2 = str(new_x) + "-" + str(y)
                if (vertex_1 in self.points) and (vertex_2 in self.points):
                    res += self.points[vertex] * self.points[vertex_1] * self.points[vertex_2]
                new_x = point[0] + delta
                vertex_1 = str(new_x) + "-" + str(point[1])
                vertex_2 = str(new_x) + "-" + str(y)
                if (vertex_1 in self.points) and (vertex_2 in self.points):
                    res += self.points[vertex] * self.points[vertex_1] * self.points[vertex_2]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
