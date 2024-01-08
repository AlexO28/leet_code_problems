# You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
# Return the number of boomerangs.
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return 0
        count = 0
        for i in range(len(points)):
            freq_dict = {}
            for j in range(len(points)):
                if i != j:
                    dist = self.distance(points[i], points[j])
                    if dist in freq_dict:
                        freq_dict[dist].append(j)
                    else:
                        freq_dict[dist] = [j]
            for key in freq_dict.keys():
                val = len(freq_dict[key])
                if val > 1:
                    count += val*(val-1)
        return count

    def distance(self, point1, point2):
        return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
