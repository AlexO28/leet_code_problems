# You are given a circle represented as (radius, xCenter, yCenter) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.
# Return true if the circle and rectangle are overlapped otherwise return false. In other words, check if there is any point (xi, yi) that belongs to the circle and the rectangle at the same time.
class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        return (
            self.getClosestDistanceToInterval(x1, x2, xCenter) ** 2
            + self.getClosestDistanceToInterval(y1, y2, yCenter) ** 2
            <= radius**2
        )

    def getClosestDistanceToInterval(self, rangeStart, rangeEnd, point):
        if rangeStart <= point <= rangeEnd:
            return 0
        if point < rangeStart:
            return rangeStart - point
        else:
            return point - rangeEnd
