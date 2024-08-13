# An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.
# Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.
# Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return self.projectionsOverlap(rec1[0], rec1[2], rec2[0], rec2[2]) and self.projectionsOverlap(rec1[1], rec1[3], rec2[1], rec2[3])

    def projectionsOverlap(self, xmin1, xmax1, xmin2, xmax2):
        if (xmin2 > xmin1) and (xmin2 < xmax1):
            return True
        elif (xmax2 > xmin1) and (xmax2 < xmax1):
            return True
        elif (xmin1 > xmin2) and (xmin1 < xmax2):
            return True
        elif (xmax1 > xmin2) and (xmax1 < xmax2):
            return True
        else:
            return False
