# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        lines = {}
        max_sum = 2
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                # (y - y2)/(y2 - y1) = (x - x2)/(x2 - x1)
                if points[j][0] == points[i][0]:
                    A = 1
                    B = 0
                    C = -points[j][0]
                elif points[j][1] == points[i][1]:
                    A = 0
                    B = 1
                    C = -points[j][1]
                else:
                    A = 1/(points[j][0] - points[i][0])
                    B = -1/(points[j][1] - points[i][1])
                    C =  (-points[j][1]*B - points[j][0]*A)
                sum_kefs = A ** 2 + B ** 2 + C ** 2
                A /= sum_kefs
                B /= sum_kefs
                C /= sum_kefs
                if ((A, B, C) not in lines.keys()):
                    summa = 0
                    for point in points:
                        if abs(A*point[0] + B*point[1] + C) <=  0.000001:
                            summa += 1
                    lines[(A, B, C)] = summa
                    max_sum = max(max_sum, summa)
        return max_sum
