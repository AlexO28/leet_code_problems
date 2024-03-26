# Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if not self.checkPointAndTriple(p1, [p2, p3, p4]):
            return False
        if not self.checkPointAndTriple(p2, [p1, p3, p4]):
            return False
        if not self.checkPointAndTriple(p3, [p1, p2, p4]):
            return False
        return True

    def checkPointAndTriple(self, point, triple):
        dist1 = self.l2_dist(point, triple[0])
        dist2 = self.l2_dist(point, triple[1])
        dist3 = self.l2_dist(point, triple[2])
        min_val = min(dist1, dist2, dist3)
        if min_val == 0:
            return False
        dist1 /= min_val
        dist2 /= min_val
        dist3 /= min_val
        distances = [dist1, dist2, dist3]
        distances.sort()
        return distances == [1.0, 1.0, 2.0]

    def l2_dist(self, point1, point2):
        return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
