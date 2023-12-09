# Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an axis-aligned rectangle. The bottom-left point of the rectangle is (xi, yi) and the top-right point of it is (ai, bi).
# Return true if all the rectangles together form an exact cover of a rectangular region.
import math


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        if len(rectangles) == 1:
            return True
        areas = 0
        xmin = math.inf
        xmax = -math.inf
        ymin = math.inf
        ymax = -math.inf
        corners = {}
        for rectangle in rectangles:
            areas += (abs(rectangle[2]-rectangle[0])*
                      abs(rectangle[3]-rectangle[1]))
            xmin = min(xmin, rectangle[0])
            xmax = max(xmax, rectangle[2])
            ymin = min(ymin, rectangle[1])
            ymax = max(ymax, rectangle[3])
            points = [str(rectangle[0]) + "-" + str(rectangle[1]),\
                      str(rectangle[2]) + "-" + str(rectangle[3]),\
                      str(rectangle[0]) + "-" + str(rectangle[3]),\
                      str(rectangle[2]) + "-" + str(rectangle[1])]
            for point in points:
                if point in corners:
                    del corners[point]
                else:
                    corners[point] = 1
        if len(corners) != 4:
            return False
        points = [str(xmin) + "-" + str(ymin),
                  str(xmax) + "-" + str(ymax),
                  str(xmin) + "-" + str(ymax),
                  str(xmax) + "-" + str(ymin)]
        for point in points:
            if point not in corners:
                return False
        if areas != abs((xmax - xmin)*(ymax-ymin)):
            return False
        return True
   
